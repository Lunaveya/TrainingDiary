from django.urls import path
from diary_app import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('today', views.today_page, name='today_page'),
]