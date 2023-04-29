from django.shortcuts import render, redirect
from .models import User

# Create your views here.
def userprofile(request):
    status = request.COOKIES.get('is_login') # 收到浏览器的再次请求,判断浏览器携带的cookie是不是登录成功的时候响应的 cookie
    if not status:
        return redirect('/authentication')
    userid = request.COOKIES.get('userid')
    user = User.objects.filter(pk=userid)
    user_name = user[0].user_name
    user_telephone = user[0].user_telephone
    user_email = user[0].user_email
    user_pwd = user[0].user_pwd
    user_address = user[0].user_address
    return render(request, "userprofile/user-profile.html", {'userid':userid, 'user_name':user_name, 'user_pwd':user_pwd, 'user_email':user_email, 'user_telephone':user_telephone, 'user_address':user_address})