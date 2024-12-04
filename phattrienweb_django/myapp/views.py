
# Create your views here
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserCreationForm
from .models import Articles
from .forms import ArticleForm  

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
    return render(request, 'articles_list.html', {'articles': articles})

def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('article_list')
    else:
        form = ArticleForm()
    return render(request, 'add_article.html', {'form': form})

# View để sửa bài viết
def edit_article(request, id):
    article = get_object_or_404(Articles, id=id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_list')
    else:
        form = ArticleForm(instance=article)
    return render(request, 'edit_article.html', {'form': form})

# View để xóa bài viết
def delete_article(request, id):
    article = get_object_or_404(Articles, id=id)
    article.delete()
    return redirect('article_list')