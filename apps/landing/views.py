from django.shortcuts import render
from django.views.generic import ListView

from apps.landing.models import Landing

class LandingView(ListView):
    model = Landing
    template_name = "landing.html"
    context_object_name = "landing"
    