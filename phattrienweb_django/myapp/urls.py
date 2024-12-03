from django.urls import path
from . import views
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('signup/', views.signup, name='signup'),  # Đăng ký
     path('login/', LoginView.as_view(), name='login'),
     path('home/', views.home, name='home'),
     path('', views.home, name='home'),
]