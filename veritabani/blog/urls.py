from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about', views.about, name='blog-about'),
    path('ilan', views.ilan, name='blog-ilan'),
    path('cv', views.cv, name='blog-Cv'),
]