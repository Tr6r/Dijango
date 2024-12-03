from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from .models import Articles


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
