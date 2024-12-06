# myapp/models.py
from django.db import models
from django.contrib.auth.models import User  # Để tham chiếu đến bảng User trong Django


# models.py
class Articles(models.Model):
    header = models.CharField(max_length=255)  # Tiêu đề bài viết
    body = models.TextField()  # Nội dung bài viết
    date = models.DateTimeField(auto_now_add=True)  # Tự động gán ngày giờ khi tạo
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )  # Khóa ngoại liên kết với bảng User

    def __str__(self):
        # Trả về cả header và một phần nội dung để dễ dàng nhận biết bài viết
        return f"{self.header} - {self.body[:50]}..."


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return self.name
