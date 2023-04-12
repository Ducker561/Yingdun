from django.shortcuts import redirect, render

# Create your views here.
# from .models import User

def index(request):
    status = request.COOKIES.get('is_login') # 收到浏览器的再次请求,判断浏览器携带的cookie是不是登录成功的时候响应的 cookie
    if not status:
        return redirect('/authentication')
    return render(request, "index/index.html")
