
from django.contrib import admin
from django.urls import path

from home import views 

urlpatterns = [
    path('',views.home, name='home'),
    path('home/',views.home, name='home'),
    path('facebook/', views.facebook, name='facebook'),
    path('instagram/', views.instagram, name='instagram'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('tictactoe/', views.tictactoe, name="tictactoe"),
    path('findthebomb/', views.findthebomb, name='findthebomb'),
    path('snake/', views.snake, name='snake'),
    
]
