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
    people_list=[1, 31, 96, 133, 218, 285, 297, 324, 333, 350, 438, 479, 514, 517, 590, 618, 660, 661, 747, 832, 868, 922, 932, 933, 960, 1008, 1022, 1029, 1071, 1074, 1122, 1153, 1156, 1163, 1193, 1234, 1259, 1280, 1290, 1337, 1340, 1351, 1367, 1417, 1418, 1453, 1525, 1537, 1613, 1627, 1700, 1714, 1769, 1865, 1881, 1889, 1929, 1944, 1985, 1998, 2044, 2076, 2078, 2146, 2161, 2162, 2168, 2189, 2219, 2243, 2246, 2317, 2354, 2380, 2399, 2441, 2461, 2527, 2588, 2597, 2676, 2685, 2737, 2737, 2819, 2868, 2903, 3009, 3108, 3110, 3137, 3157, 3163, 3248, 3334, 3349, 3362, 3378, 3384, 3450, 3468, 3470, 3569, 3591, 3647, 3657, 3696, 3709, 3747, 3819, 3867, 3911, 3923, 3942, 3975, 4089, 4092, 4097, 4152, 4166, 4264, 4267, 4276, 4368, 4378, 4401, 4453, 4461, 4507, 4528, 4552, 4573, 4610, 4620, 4649, 4730, 4731, 4752, 4780, 4819, 4935, 5018, 5021, 5063, 5113, 5123, 5142, 5153, 5160, 5161, 5167, 5169, 5186, 5188, 5256, 5262, 5323, 5371, 5378, 5427, 5446, 5448, 5610, 5638, 5685, 5688, 5713, 5740, 5752, 5800, 5829, 5843, 5890, 5922, 6009, 6081, 6098, 6122, 6130, 6236, 6241, 6266, 6366, 6372, 6380, 6380, 6395, 6485, 6500, 6577, 6586, 6633, 6636, 6641, 6753, 6769, 6772, 6794, 6804, 6831, 6845, 6863, 6898, 6995, 7007, 7031, 7040, 7043, 7102, 7130, 7230, 7264, 7277, 7310, 7373, 7411, 7450, 7478, 7516, 7566, 7606, 7670, 7700, 7708, 7751, 7770, 7836, 7966, 7993, 7998, 8020, 8032, 8050, 8076, 8105, 8126, 8130, 8205, 8210, 8248, 8345, 8358, 8418, 8472, 8490, 8521, 8620, 8670, 8783, 8829, 8895, 8922, 8955]
    for people in people_list:
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
        people_obj= People.objects.filter(pk=people)
        if len(people_obj) == 1:
            people_dict["people_no"]=people_obj[0].people_no
            people_dict["people_name"]=people_obj[0].people_name
            people_dict["people_nickname"]=people_obj[0].people_nickname
            people_dict["people_pic"]=people_obj[0].people_pic
            people_dict["people_date"]=people_obj[0].people_date
            people_dict["people_ip"]=people_obj[0].people_ip
            people_dict["people_contacts"]=people_obj[0].people_contacts
            people_dict["people_revcontacts"]=people_obj[0].people_revcontacts
            people_dict["people_pastmovie"]=people_obj[0].people_pastmovie
            people_return.append(people_dict)
    
    return render(request, "spammer/spammer.html", {"people_return":people_return})

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