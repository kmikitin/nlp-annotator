from django.shortcuts import render

from .models import Annotation, Entity, File

# Create your views here.
class AnnotationCreateView(CreateView, SuccessMessageMixin):
    template = 'annotation_create.html'
    model = Annotation
    success_message = 'New annotation set created!'

class FileUploadView(CreateView):





