from django.urls import path
from base import views 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='base/login.html'),name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='base/home.html')),
]