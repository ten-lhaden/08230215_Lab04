from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index_html'),
    path('about/', views.about_me, name='about_me'),
    path('aboutMe.html', views.about_me, name='about_me_html'),
]

