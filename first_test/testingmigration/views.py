from django.shortcuts import render
from django.http import HttpResponse

def test(request):
    return HttpResponse("<h2>this is test!</h2>")