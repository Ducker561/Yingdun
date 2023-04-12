from django.shortcuts import redirect, render
from django.http import JsonResponse

# Create your views here.
from .models import User

def index(request):
    return render(request, "authentication/signin.html")

def login(request):
    userid = dict(request.POST).get('userid')[0]
    userpwd = dict(request.POST).get('userpwd')[0]
    try:
        user = User.objects.filter(pk=userid, user_pwd = userpwd)
        if len(user) == 1:
            return JsonResponse({'res':1})
        else:
            return JsonResponse({'res':0})
    except:
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