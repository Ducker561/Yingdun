from hashlib import md5
import random
import string
from django.shortcuts import redirect, render
from django.http import JsonResponse

# Create your views here.
from .models import User

def index(request):
    return render(request, "authentication/signin.html")

def login(request):
    userid = request.POST.get('userid')
    userpwd = request.POST.get('userpwd')
    userpwd = md5(userpwd.encode()).hexdigest()
    try:
        user = User.objects.filter(pk=userid, user_pwd = userpwd)
        if len(user) == 1:
            rep = redirect("/")
            random_str = ''.join(random.sample(string.ascii_letters + string.digits, 32))
            rep.set_cookie("is_login", random_str)
            return rep
            return JsonResponse({'res':1})
        else:
            error_msg = '用户名或密码错误，请重新输入。'
            return redirect("/authentication")
            return JsonResponse({'res':0})
    except:
        error_msg = '发生内部错误，请重试。'
        return redirect("/authentication")
        return JsonResponse({'res':0})

def register(request):
    return render(request, "authentication/register.html")

def register_user(request):
    username = dict(request.POST).get('username')[0]
    useremail = dict(request.POST).get('useremail')[0]
    userpwd = dict(request.POST).get('userpwd')[0]
    # User.objects.create(user_name=username, user_email=useremail, user_pwd=userpwd)
    user = User()
    user_list=User.objects.filter(user_email=useremail)
    if len(user_list)!=0:
        return JsonResponse({'res':0})
    user.user_name = username
    user.user_email = useremail
    user.user_pwd = userpwd
    user.save()
    return JsonResponse({'res':user.user_id})