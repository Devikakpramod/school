from django.urls import path
from django.contrib import messages
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('form/', views.form, name='form'),
    path('formfill/', views.formfill, name='formfill'),
    path('data/', views.data, name='data'),
]
