from django.contrib import admin

# Register your models here.
from .models import Articles  # Nhập model Articles từ myapp/models.py

class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('header', 'user', 'date')  # Hiển thị các trường trong bảng admin
    search_fields = ('header', 'body')  # Các trường có thể tìm kiếm
    list_filter = ('user', 'date')  # Bộ lọc cho các trường 'user' và 'date'

# Đăng ký model Articles vào admin
admin.site.register(Articles, ArticlesAdmin)