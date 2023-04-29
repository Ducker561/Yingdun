from django.shortcuts import redirect, render
from .models import Comment, Movie
from random import *
import random

# Create your views here.
# from .models import User

def index(request):
    # 生成随机数显示spam评论
    seed(a=None)
    randomlist=[]
    for randomnum in range(8):
        randomnum=random.randint(1,16340)
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
    return render(request, "index/index.html", {"count_spam_total":count_spam_total,
                                                "comment1":comment1[:23],
                                                "comment2":comment2[:23],
                                                "comment3":comment3[:23],
                                                "comment4":comment4[:23],
                                                "comment5":comment5[:23],
                                                "comment6":comment6[:23],
                                                "comment7":comment7[:23],
                                                "comment8":comment8[:23],
                                                })
