import re
import random

import spacy
from spacy.util import minibatch, compounding

import tika
tika.initVM()
from tika import parser

from django.shortcuts import render
from django import forms
from django.views.generic.edit import CreateView

from .models import Annotation, Entity

# Create your views here.
class AnnotationCreateForm(forms.ModelForm):
    class Meta:
        model = Annotation
        fields = ['file_name', 'file']


class AnnotationCreateView(CreateView):
    template = 'annotation_create.html'
    model = Annotation
    form_class = AnnotationCreateForm









