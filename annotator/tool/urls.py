from django.urls import path, re_path, include
from .views import AnnotationCreateView, AnnotationListView, AnnotationDetailView

urlpatterns = [
    path('annotations/new/', AnnotationCreateView.as_view(), name='new_annotation'),
    path('annotations/', AnnotationListView.as_view(), name='annotations'),
    re_path('annotations/(?P<pk>\d+)', AnnotationDetailView.as_view(), name='detail_annotation'),
]

