from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'InterChangeMoney/$', views.InterChangeMoneyUrls.as_view()),
    url(r'InterChangeMoney/Balance', views.MoneyOperations.as_view()),
    url(r'InterChangeMoney/Operation', views.MoneyOperations.as_view()),
    url(r'InterChangeMoney/TransferMoney/', views.MoneyOperations.as_view()),

]