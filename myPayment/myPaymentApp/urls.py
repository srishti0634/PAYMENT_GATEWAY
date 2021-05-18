from django.urls import path
from myPaymentApp import views

urlpatterns =[
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('fieldsDetail/', views.fieldsDetail, name="fieldsDetail"),
    path('success/', views.success, name="success"),
]
