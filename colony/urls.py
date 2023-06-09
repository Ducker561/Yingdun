from django.urls import path

from . import views

app_name = "colony"
urlpatterns = [
    # ex: /spammer
    path("", views.colony, name="colony"),
    # ex: /spammer/detail/
    # path("detail/<int:people_nickname>/", views.detail, name="detail"),
    # path("detail/", views.detail_redirect, name="detail_redirect"),
    # # ex: /polls/5/results/
    # path("<int:question_id>/results/", views.results, name="results"),
    # # ex: /polls/5/vote/
    # path("<int:question_id>/vote/", views.vote, name="vote"),
]