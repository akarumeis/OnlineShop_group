from django.urls import path, include
from . views import showMain, showCatalog, showFeedback, showAboutus

urlpatterns = [
    path('aboutus/', showAboutus, name='aboutus'),
    path('feedback/', showFeedback, name='feedback'),
    path('catalog/', showCatalog, name='catalog'),
    path('main/', showMain, name='main'),
]
