from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('login-register/', views.loginRegisterPage, name='login-register')
]