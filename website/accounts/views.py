from django.shortcuts import render
from django.views.generic import TemplateView
from allauth.account.views import SignupView, LoginView
# Create your views here.

class ProfileView(TemplateView):
    template_name = 'dashboard/profile.html'

    def get_queryset(self):
        self.id = self.kwargs['id']
        queryset = super(ProfileView, self).get_queryset()
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwartgs)
        context['id'] = self.id
        return context