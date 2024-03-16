from django.urls import path
from apps.views import index, index2

urlpatterns = [
    path('home', index, name='home'),
    path('about', index2, name='about')
]
