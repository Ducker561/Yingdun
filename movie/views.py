from django.shortcuts import redirect, render
from .models import Comment, Movie
import jieba
import collections
import re
from wordcloud import WordCloud
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

# Create your views here.    

def draw_word_cloud(movie_no, all_comments):
    # 绘制词云
    if os.path.exists('./public_static/wordcloud_images/{}.png'.format(movie_no)):
        pass
    else:
        # 评论数据
        data = all_comments
        
        # 文本预处理  去除一些无用的字符   只提取出中文出来
        new_data = re.findall('[\u4e00-\u9fa5]+', data, re.S)
        new_data = " ".join(new_data)
            
        # 文本分词
        seg_list_exact = jieba.cut(new_data, cut_all=True)
        
        result_list = []
        with open('./movie/stopWord.txt', encoding='utf-8') as f:
            con = f.readlines()
            stop_words = set()
            for i in con:
                i = i.replace("\n", "")   # 去掉读取每一行数据的\n
                stop_words.add(i)
            
        for word in seg_list_exact:
            # 设置停用词并去除单个词
            if word not in stop_words and len(word) > 1:
                result_list.append(word)
            
        # 筛选后统计
        word_counts = collections.Counter(result_list)
        # 获取前100最高频的词
        word_counts_top100 = word_counts.most_common(100)
            
        # 绘制词云
        my_cloud = WordCloud(
            background_color='white',  # 设置背景颜色  默认是black
            width=900, height=825,
            max_words=150,            # 词云显示的最大词语数量
            font_path='simhei.ttf',   # 设置字体  显示中文
            max_font_size=99,         # 设置字体最大值
            min_font_size=16,         # 设置子图最小值
            random_state=50           # 设置随机生成状态，即多少种配色方案
        ).generate_from_frequencies(word_counts)
        plt.imshow(my_cloud, interpolation='bilinear')
        plt.axis('off')
        plt.savefig('./public_static/wordcloud_images/{}.png'.format(movie_no), bbox_inches='tight', pad_inches=0, dpi=1000) 

def movie(request):
    status = request.COOKIES.get('is_login') # 收到浏览器的再次请求,判断浏览器携带的cookie是不是登录成功的时候响应的 cookie
    if not status:
        return redirect('/authentication')
    moive_name_user = request.GET.get('moive_name_user')
    count_spam = 0
    real_rating = 0
    rating = 0
    our_database_rating = 0
    voting = 0
    spam_voting = 0
    influence = 0
    movie_name = None
    movie_no = 404
    comment = None
    all_comments=""
    if moive_name_user is None:
        moive_name_user = "阿凡达"  # 默认 阿凡达
    movie = Movie.objects.filter(movie_name__contains=moive_name_user)
    if len(movie) == 1:
        movie_no = movie[0].movie_no
        movie_name = movie[0].movie_name
        rating = movie[0].movie_score
        comment = Comment.objects.filter(movie_no=movie[0].movie_no)
        for comm in comment:
            voting += comm.comment_vote
            our_database_rating += comm.comment_rating
            all_comments+=comm.comment_content
            if comm.comment_isspam == 1:
                count_spam+=1
                spam_voting += comm.comment_vote
            else:
                real_rating += comm.comment_rating
        real_rating = format(2*real_rating/(len(comment)-count_spam), '.1f')
        our_database_rating = format(2*our_database_rating/len(comment), '.1f')
        influence = format(spam_voting/voting, '.2f')

        draw_word_cloud(movie_no=movie_no, all_comments=all_comments)

    else:
        # count_spam = "未查询到电影"
        movie_name = '未查询到"{}"电影'.format(moive_name_user)
        comment = []

    return render(request, "movie/movie.html", {"movie_name":movie_name,"count_spam":count_spam, "real_rating":real_rating, "rating":rating, "count_comment":len(comment), "influence":influence, "wordcloud":movie_no})

def detail(request):
    status = request.COOKIES.get('is_login') # 收到浏览器的再次请求,判断浏览器携带的cookie是不是登录成功的时候响应的 cookie
    if not status:
        return redirect('/authentication')
    moive_name_user = request.GET.get('moive_name_user')
    if moive_name_user is None:
        moive_name_user = "阿凡达"  # 默认 阿凡达
    movie_pic="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fsafe-img.xhscdn.com%2Fbw1%2F159d3477-06cd-40ed-af19-d4686b910e46%3FimageView2%2F2%2Fw%2F1080%2Fformat%2Fjpg&refer=http%3A%2F%2Fsafe-img.xhscdn.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1685119601&t=e804ea0e80b04c17497b788135f021f9"
    movie_name=""
    movie_no=404
    movie_rating=0
    movie_intro="请检查您的输入"
    movie_genres="未知"
    movie_region="未知地区"
    movie_actor=""
    movie_release="0000-00-00"
    movie_emotion="0.0"
    all_comments=""
    movie = Movie.objects.filter(movie_name__contains=moive_name_user)
    if len(movie) == 1:
        movie_no=movie[0].movie_no
        movie_pic=movie[0].movie_pic
        movie_name=movie[0].movie_name
        movie_rating=movie[0].movie_score
        movie_intro=movie[0].movie_intro.replace("\n","").replace("\t","").replace("\r","").replace("\u3000","").replace(" ","")
        movie_genres=movie[0].movie_genres
        movie_region=movie[0].movie_country
        movie_release=movie[0].movie_realease
        movie_actor=movie[0].movie_actor
        movie_emotion=movie[0].movie_emotion
        comment = Comment.objects.filter(movie_no=movie_no)
        for comm in comment:
            all_comments+=comm.comment_content

        draw_word_cloud(movie_no=movie_no, all_comments=all_comments)
    else:
        # count_spam = "未查询到电影"
        movie_name = '未查询到"{}"电影'.format(moive_name_user)
        comment = []

    return render(request, "movie/moviedetail.html",{"movie_emotion":movie_emotion,"wordcloud":movie_no,"movie_pic":movie_pic,"movie_name":movie_name,"movie_rating":movie_rating,"movie_intro":movie_intro,"movie_genres":movie_genres,"movie_region":movie_region,"movie_release":movie_release,"movie_actor":movie_actor})