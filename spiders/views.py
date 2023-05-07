from django.shortcuts import render, redirect

# Create your views here.
def spiders(request):
    status = request.COOKIES.get('is_login') # 收到浏览器的再次请求,判断浏览器携带的cookie是不是登录成功的时候响应的 cookie
    if not status:
        return redirect('/authentication')
    return render(request, "spiders/spiders.html")