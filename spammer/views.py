from random import seed
import random
from django.shortcuts import redirect, render
from .models import People

# Create your views here.

def spammer(request):
    status = request.COOKIES.get('is_login') # 收到浏览器的再次请求,判断浏览器携带的cookie是不是登录成功的时候响应的 cookie
    if not status:
        return redirect('/authentication/')
    people_return = []
    people_dict={
        "people_no":0,
        "people_name":"",
        "people_nickname":"",
        "people_pic":"",
        "people_date":"",
        "people_ip":"",
        "people_contacts":0,
        "people_revcontacts":0,
        "people_pastmovie":""
    }
    nice_list=People.objects.filter(people_isspam=0)
    people_list=People.objects.filter(people_isspam=1)
    count_spammer=len(people_list)
    count_nice=len(nice_list)
    for people_obj in people_list:
        people_dict={
            "people_no":0,
            "people_name":"",
            "people_nickname":"",
            "people_pic":"",
            "people_date":"",
            "people_ip":"",
            "people_contacts":0,
            "people_revcontacts":0,
            "people_pastmovie":""
        }
        people_dict["people_no"]=people_obj.people_no
        people_dict["people_name"]=people_obj.people_name
        people_dict["people_nickname"]=people_obj.people_nickname
        people_dict["people_pic"]=people_obj.people_pic
        people_dict["people_date"]=people_obj.people_date
        people_dict["people_ip"]=people_obj.people_ip
        people_dict["people_contacts"]=people_obj.people_contacts
        people_dict["people_revcontacts"]=people_obj.people_revcontacts
        people_dict["people_pastmovie"]=people_obj.people_pastmovie
        people_return.append(people_dict)
    
    return render(request, "spammer/spammer.html", {"people_return":people_return, "count_spammer":count_spammer, "spammer_rate":format(100*(count_spammer/(count_spammer+count_nice)),'.2f')})

def detail(request, people_nickname=100009133):
    status = request.COOKIES.get('is_login') # 收到浏览器的再次请求,判断浏览器携带的cookie是不是登录成功的时候响应的 cookie
    if not status:
        return redirect('/authentication/')
    people_dict={
        "people_no":0,
        "people_name":"",
        "people_nickname":"",
        "people_pic":"",
        "people_date":"",
        "people_ip":"",
        "people_contacts":0,
        "people_revcontacts":0,
        "people_pastmovie":""
    }
    people_obj= People.objects.filter(people_nickname=people_nickname)
    if len(people_obj) == 1:
            people_dict["people_no"]=people_obj[0].people_no
            people_dict["people_name"]=people_obj[0].people_name
            people_dict["people_nickname"]=people_obj[0].people_nickname
            people_dict["people_pic"]=people_obj[0].people_pic
            people_dict["people_date"]=people_obj[0].people_date
            people_dict["people_ip"]=people_obj[0].people_ip
            people_dict["people_contacts"]=people_obj[0].people_contacts
            people_dict["people_revcontacts"]=people_obj[0].people_revcontacts
            people_dict["people_pastnum"]=people_obj[0].people_pastnum
            people_dict["people_nownum"]=people_obj[0].people_nownum
            people_dict["people_wantnum"]=people_obj[0].people_wantnum

    return render(request, "spammer/spammerdetail.html",{"people_dict":people_dict})

def detail_redirect(request):
    status = request.COOKIES.get('is_login') # 收到浏览器的再次请求,判断浏览器携带的cookie是不是登录成功的时候响应的 cookie
    if not status:
        return redirect('/authentication/')
    return redirect("/spammer/detail/100009133/")