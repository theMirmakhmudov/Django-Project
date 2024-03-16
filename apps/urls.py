from django.urls import path
from apps.views import index, index2, index3

urlpatterns = [
    path('home', index, name='home'),
    path('about', index2, name='about'),
    path('',index3, name='index')
]
