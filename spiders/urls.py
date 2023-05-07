from django.urls import path

from . import views

app_name = "spiders"
urlpatterns = [
    # ex: /spiders
    path("", views.spiders, name="spiders"),
    # ex: /movie/moviedetail
    # path("moviedetail/", views.detail, name="detail"),
    # # ex: /polls/5/results/
    # path("<int:question_id>/results/", views.results, name="results"),
    # # ex: /polls/5/vote/
    # path("<int:question_id>/vote/", views.vote, name="vote"),
]