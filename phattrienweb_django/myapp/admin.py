from django.contrib import admin
from django.shortcuts import redirect
# Register your models here.
from .models import Articles  

class ArticlesAdmin(admin.ModelAdmin):
    # Ghi đè trang mặc định để chuyển hướng trực tiếp
    def changelist_view(self, request, extra_context=None):
        # Redirect tới trang custom view
        return redirect('article_list')  # Điều hướng tới view 'article_list'

# Đăng ký model với admin
admin.site.register(Articles, ArticlesAdmin)