from django.shortcuts import render

# Create your views here.
# from .models import User

def index(request):
    return render(request, "index/index.html")
