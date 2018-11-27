from django.urls import path, include
from .views import AnnotationCreateView, AnnotationListView

urlpatterns = [
    path('annotations/new/', AnnotationCreateView.as_view(), name='new_annotation'),
    path('annotations/', AnnotationListView.as_view(), name='annotations'),
]

