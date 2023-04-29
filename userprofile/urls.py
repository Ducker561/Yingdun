from django.urls import path

from . import views

app_name = "userprofile"
urlpatterns = [
    # ex: /userprofile
    path("", views.userprofile, name="userprofile"),
    # ex: /authentication/check_login/
    # path("check_login/", views.login, name="login"),
    # # ex: /polls/5/results/
    # path("<int:question_id>/results/", views.results, name="results"),
    # # ex: /polls/5/vote/
    # path("<int:question_id>/vote/", views.vote, name="vote"),
]