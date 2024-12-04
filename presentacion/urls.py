
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('qr/', views.qr_code, name='qr_code'),
]