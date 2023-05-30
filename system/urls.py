from django.urls import path

from . import views

app_name = "system"
urlpatterns = [
    # ex: /system/hardware
    path("hardware/", views.hardware, name="hardware"),
    # ex: /system/hardware/get_cpu_percentage
    path("hardware/get_cpu_percentage/", views.get_cpu_percentage, name="get_cpu_percentage"),
    # # ex: /polls/5/results/
    # path("<int:question_id>/results/", views.results, name="results"),
    # # ex: /polls/5/vote/
    # path("<int:question_id>/vote/", views.vote, name="vote"),
]