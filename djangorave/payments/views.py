from django.shortcuts import render

# Create your views here.
from django.conf import settings
from django.views.generic.base import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['key'] = settings.RAVE_PUBLIC_KEY
        context['logo'] = settings.WILDLIFE_LOGO
        return context

class Success(TemplateView):
    template_name = 'success.html'

