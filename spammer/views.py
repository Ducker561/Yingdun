from django.shortcuts import render

# Create your views here.

def show_spammer(request):
    return render(request, "spammer/spammer.html")