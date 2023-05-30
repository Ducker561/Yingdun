from django.urls import path

from . import views

app_name = "alarm"
urlpatterns = [
    # ex: /spammer
    path("", views.alarm, name="alarm"),
]