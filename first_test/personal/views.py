from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'personal/layout.html')

#def home(request):
    #return render(request, 'personal/home.html')

def home(request):
    return HttpResponse("<h2>from views.py home()!</h2>")



