from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse, redirect
import random

# Create your views here.
GOLD_MAP = {
    "farm": (10, 20),
    "cave": (5, 10),
    "house": (2, 5),
    "casino": (0, 50)
}


def index(request):
    return render(request, 'index.html')


yourgold = 0


def process(request):
    if 'name' == 'farm':
        request.session['farm'] = request.POST['farm']
        yourgold += random(10-20)


def gold(request):
    pass
