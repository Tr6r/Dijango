# Create your views here
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserCreationForm
from .models import Articles, Contact
from .forms import ArticleForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponse


def admin_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/myapp/admin/")  # Đăng nhập xong quay về admin
        else:
            return render(request, "admin_login.html", {"error": "Invalid credentials"})
    else:
        return render(request, "admin_login.html")


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")  # Redirect to login page after registration
    else:
        form = CustomUserCreationForm()

    return render(request, "signup.html", {"form": form})


def home(request):
    posts = Articles.objects.all()  # Lấy tất cả bài viết từ cơ sở dữ liệu
    return render(request, "blog/home.html", {"posts": posts})


def about(request):
    return render(request, "blog/about.html", {"title": "About"})


def article_list(request):
    articles = Articles.objects.all()
    return render(request, "articles_list.html", {"articles": articles})


def add_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("article_list")
    else:
        form = ArticleForm()
    return render(request, "add_article.html", {"form": form})


# View để sửa bài viết
def edit_article(request, id):
    article = get_object_or_404(Articles, id=id)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect("article_list")
    else:
        form = ArticleForm(instance=article)
    return render(request, "edit_article.html", {"form": form})


# View để xóa bài viết
def delete_article(request, id):
    article = get_object_or_404(Articles, id=id)
    article.delete()
    return redirect("article_list")


def contact(request):
    if request.method == "POST":
        # Lấy dữ liệu từ form
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # Lưu thông tin vào cơ sở dữ liệu
        contact = Contact(name=name, email=email, message=message)
        contact.save()  # Lưu vào bảng Contact trong cơ sở dữ liệu

        return render(request, "blog/contact.html", {"success": True})
    return render(request, "blog/contact.html")
