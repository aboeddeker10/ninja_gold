from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse, redirect
import random


def index(request):
    if not "gold" in request.session or "activities" not in request.session:
        request.session["gold"] = 0
        request.session["activities"] = []
    return render(request, 'index.html')


def gold(request):
    print(f'Your gold is currently: {request.session["gold"]}')
    if request.POST['building'] == 'cave':
        addedGold = random.randint(5, 10)
        request.session['gold'] += addedGold
        request.session['activities'].append(
            f'You went to cave and received {addedGold} and now you have a total of {request.session["gold"]}')
    if request.POST['building'] == 'house':
        addedGold = random.randint(2, 5)
        request.session['gold'] += addedGold
        request.session['activities'].append(
            f'You went to house and received {addedGold} and now you have a total of {request.session["gold"]}')
    if request.POST['building'] == 'farm':
        addedGold = random.randint(10, 20)
        request.session['gold'] += addedGold
        request.session['activities'].append(
            f'You went to farm and received {addedGold} and now you have a total of {request.session["gold"]}')
    if request.POST['building'] == 'casino':
        addedGold = random.randint(-50, 50)
        request.session['gold'] += addedGold
        request.session['activities'].append(
            f'You went to casino and received {addedGold} and now you have a total of {request.session["gold"]} ')
    print(f'Your gold has been updated to: {request.session["gold"]}')
    return redirect('/')


def reset(request):
    request.session.flush()
    return redirect('/')
