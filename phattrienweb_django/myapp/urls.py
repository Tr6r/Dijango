from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path("admin_login/", views.admin_login, name="custom_admin_login"),
    path("signup/", views.signup, name="signup"),  # Đăng ký
    path("login/", LoginView.as_view(), name="login"),
    path("home/", views.home, name="home"),
    path("about/", views.about, name="blog-about"),
    path("", views.home, name="blog-home"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("contact/", views.contact, name="contact"),
    path("admin/articles/", views.article_list, name="article_list"),
    path("admin/articles/add/", views.add_article, name="add_article"),  # Thêm bài viết
    path(
        "admin/articles/edit/<int:id>/", views.edit_article, name="edit_article"
    ),  # Sửa bài viết
    path(
        "admin/articles/delete/<int:id>/", views.delete_article, name="delete_article"
    ),  # Xóa bài viết
]
