import json
from django.shortcuts import redirect, render
from .models import Comment, Movie, People
from random import *
import random

# Create your views here.
# from .models import User

def index(request):
    ip_dict={
        '河北':0,
        '山西':0,
        '黑龙江':0,
        '吉林':0,
        '辽宁':0,
        '江苏':0,
        '浙江':0,
        '安徽':0,
        '福建':0,
        '江西':0,
        '山东':0,
        '河南':0,
        '湖北':0,
        '湖南':0,
        '广东':0,
        '海南':0,
        '四川':0,
        '贵州':0,
        '云南':0,
        '陕西':0,
        '甘肃':0,
        '青海':0,
        '中国台湾':0,
        '内蒙古':0,
        '广西':0,
        '西藏':0,
        '宁夏':0,
        '新疆':0,
        '北京':0,
        '天津':0,
        '上海':0,
        '重庆':0,
        '中国香港':0,
        '中国澳门':0,
        '海外':0,
    }
    people_list=People.objects.filter(people_isspam=1)
    count_spammer=len(people_list)
    return_ip_list=[]
    for people in people_list:
        try:
            ip_dict[people.people_ip]+=1
        except KeyError:
            ip_dict['海外']+=1
    for location, count_number in ip_dict.items():
        if location=="中国香港":
            location="香港"
        elif location=="中国澳门":
            location="澳门"
        elif location=="中国台湾":
            location="台湾"
        temp={'name':location, 'value':count_number}
        return_ip_list.append(temp)
    return_ip_list.append({'name':'南海诸岛', 'value':0})

    # 生成随机数显示spam评论
    seed(a=None)
    randomlist=[]
    for randomnum in range(10):
        randomnum=random.randint(1,16000)
        randomlist.append(randomnum)
    randomlist.sort()

    count_spam_total=0
    movies = Movie.objects.all()
    commnet1=""
    commnet2=""
    commnet3=""
    commnet4=""
    commnet5=""
    commnet6=""
    commnet7=""
    commnet8=""
    commnet9=""
    commnet10=""
    for movie in movies:
        comments = Comment.objects.filter(movie_no=movie.movie_no)
        for comment in comments:
            if comment.comment_isspam==1:
                count_spam_total+=1
                if randomlist[0]==count_spam_total:
                    comment1 = comment.comment_username+"："+comment.comment_content.replace("\n"," ").replace("\r"," ").replace("\t"," ")
                if randomlist[1]==count_spam_total:
                    comment2 = comment.comment_username+"："+comment.comment_content.replace("\n"," ").replace("\r"," ").replace("\t"," ")
                if randomlist[2]==count_spam_total:
                    comment3 = comment.comment_username+"："+comment.comment_content.replace("\n"," ").replace("\r"," ").replace("\t"," ")
                if randomlist[3]==count_spam_total:
                    comment4 = comment.comment_username+"："+comment.comment_content.replace("\n"," ").replace("\r"," ").replace("\t"," ")
                if randomlist[4]==count_spam_total:
                    comment5 = comment.comment_username+"："+comment.comment_content.replace("\n"," ").replace("\r"," ").replace("\t"," ")
                if randomlist[5]==count_spam_total:
                    comment6 = comment.comment_username+"："+comment.comment_content.replace("\n"," ").replace("\r"," ").replace("\t"," ")
                if randomlist[6]==count_spam_total:
                    comment7 = comment.comment_username+"："+comment.comment_content.replace("\n"," ").replace("\r"," ").replace("\t"," ")
                if randomlist[7]==count_spam_total:
                    comment8 = comment.comment_username+"："+comment.comment_content.replace("\n"," ").replace("\r"," ").replace("\t"," ")
                if randomlist[8]==count_spam_total:
                    comment9 = comment.comment_username+"："+comment.comment_content.replace("\n"," ").replace("\r"," ").replace("\t"," ")
                if randomlist[9]==count_spam_total:
                    comment10 = comment.comment_username+"："+comment.comment_content.replace("\n"," ").replace("\r"," ").replace("\t"," ")
    return render(request, "index/index.html", {"count_spam_total":count_spam_total,
                                                "comment1":comment1[:23],
                                                "comment2":comment2[:23],
                                                "comment3":comment3[:23],
                                                "comment4":comment4[:23],
                                                "comment5":comment5[:23],
                                                "comment6":comment6[:23],
                                                "comment7":comment7[:23],
                                                "comment8":comment8[:23],
                                                "comment9":comment9[:23],
                                                "comment10":comment10[:23],
                                                "count_spammer":count_spammer,
                                                "return_ip_list":return_ip_list})
