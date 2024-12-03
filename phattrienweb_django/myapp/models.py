# myapp/models.py
from django.db import models
from django.contrib.auth.models import User  # Để tham chiếu đến bảng User trong Django

class Articles(models.Model):
    header = models.CharField(max_length=255)  # Tiêu đề bài viết
    body = models.TextField()  # Nội dung bài viết
    date = models.DateTimeField(auto_now_add=True)  # Tự động gán ngày giờ khi tạo
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Khóa ngoại liên kết với bảng User

    # Hàm để hiển thị tiêu đề của bài viết khi in ra đối tượng
    def __str__(self):
        return self.header