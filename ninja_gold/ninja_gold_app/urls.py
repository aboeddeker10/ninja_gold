from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('gold', views.gold),
    path('reset', views.reset)
]
