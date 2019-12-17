import re
import random

import spacy
from spacy.util import minibatch, compounding

import tika
tika.initVM()
from tika import parser

from django.shortcuts import render, redirect
from django import forms
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .models import Annotation, Entity, Label


class AnnotationCreateForm(forms.ModelForm):
    class Meta:
        model = Annotation
        fields = ['file_name', 'file']


class AnnotationCreateView(CreateView):
    model = Annotation
    form_class = AnnotationCreateForm


    def create_entities(self, label, words):
        ent_list = []
        for num, word in enumerate(words):
            entity = Entity()

            label = Label.objects.get(name=label)

            entity.start = word.start()
            entity.end = word.end()
            entity.phrase = word.group()
            entity.entity_type = label
            entity.save()

            ent_list.append(entity) 
        return ent_list

    def get_annotations(self, file):
        nlp = spacy.load('en_core_web_lg')
        parsed = parser.from_file('../media/' + file)
        
        try:
            doc = nlp(parsed['content'])
            ent_list = []

            for ent in doc.ents:
                entity = Entity()
                label = Label.objects.get(name=ent.label_)
                print(label)
                entity.entity_type = label
                entity.phrase = ent.text 
                entity.start = ent.start_char
                entity.end = ent.end_char
                entity.save()
                ent_list.append(entity)
            
            icd10_codes = re.finditer(r'[A-Z]\d{2}\s|[A-Z]\d{2}\.[A-Z0-9]{0,4}', doc.text)
            hcpcs_codes = re.finditer(r'[A-Z]\d{4}', doc.text)
            cpt_codes = re.finditer(r'\b\d{5}\b|\d{4}(T|F)', doc.text)

            if icd10_codes:
                ent_list += self.create_entities('ICD10_CODE', icd10_codes)

            if hcpcs_codes:
                ent_list += self.create_entities('HCPCS_CODE', hcpcs_codes)

            if cpt_codes:
                ent_list += self.create_entities('CPT_CODE', cpt_codes)

            return doc.text, ent_list

        except ValueError:
            raise ValidationError('Tika can\'t parse that document, please choose a different one', code='invalid')

    def post(self, request, *args, **kwargs):
        form = AnnotationCreateForm(request.POST, request.FILES)

        if form.is_valid():
            annotation = form.save()
            text, entities = self.get_annotations(annotation.file.name)
            annotation.text = text
            annotation.entities.set(entities)
            annotation.save()
        else:
            return render(request, self.template, form)

        return redirect('detail_annotation', pk=annotation.pk)


class AnnotationListView(ListView):
    model = Annotation

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['annotations'] = Annotation.objects.all()
        return context


class AnnotationDetailView(DetailView):
    model = Annotation

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['annotation'] = kwargs['object']
        return context


class AnnotationAnnotateView(UpdateView):
    model = Annotation





