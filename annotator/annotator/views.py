from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView

class HomePageView(TemplateView):
    template_name = 'base_site.html'

