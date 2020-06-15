# pages/urls.py
from django.urls import path
from . import views

app_name="pages"

urlpatterns = [
    path('index/', views.index, name="index"),
    path('food/<str:name>/', views.food, name="food"),
    path('throw/', views.throw, name="throw"),
    path('catch/', views.catch, name="catch"),
    path('lotto/', views.lotto, name="lotto"),
    path('lotto_result/', views.lotto_result, name="lotto_result"),
    path('artii/', views.artii, name="artii"),
    path('result/', views.result, name="result"),
]