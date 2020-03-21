from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class AboutView(TemplateView):
    template_name = 'pages/about.html'

class ContactView(TemplateView):
    template_name = 'pages/contact.html'

class DemoesView(TemplateView):
    template_name = 'pages/demoes.html'

class PortfolioView(TemplateView):
    template_name = 'pages/portfolio.html'