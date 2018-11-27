from django.urls import path, include
from .views import AnnotationCreateView

urlpatterns = [
    path('annotations/new/', AnnotationCreateView.as_view(), name='annotation_create'),
]

