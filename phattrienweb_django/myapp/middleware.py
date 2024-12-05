from django.shortcuts import redirect

class AdminLoginRequiredMiddleware:
 
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Nếu URL bắt đầu bằng '/admin/' và người dùng chưa đăng nhập
        print(request.user.is_authenticated)
        if request.path.startswith('/myapp/admin/') and not request.user.is_authenticated:
            print("hehehe")

            return redirect('custom_admin_login') # Chuyển hướng đến trang login custom
        
        # Chuyển yêu cầu đến tầng tiếp theo
        response = self.get_response(request)
        return response
