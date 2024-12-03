from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import admin


urlpatterns = [
    path("signup/", views.signup, name="signup"),  # Đăng ký
    path("login/", LoginView.as_view(), name="login"),
    path("home/", views.home, name="home"),
    path("about/", views.about, name="blog-about"),
    path("", views.home, name="blog-home"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("admin/", admin.site.urls, name="admin"),
]
