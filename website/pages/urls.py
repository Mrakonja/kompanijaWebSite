from django.urls import path
from .views import AboutView, ContactView, DemoesView, PortfolioView

urlpatterns = [
    path('', AboutView.as_view(), name='about'),
    path('contact', ContactView.as_view(), name='contact'),
    path('portfolio', PortfolioView.as_view(), name='portfolio'),
    path('demoes', DemoesView.as_view(), name='demoes'),

    ]
