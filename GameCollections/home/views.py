from django.shortcuts import render
from django.http import HttpResponseRedirect
def home(request):
    return render (request, 'home.html')

def facebook(request):
    return HttpResponseRedirect('https://www.facebook.com/heyitspiyush')  

def instagram(request):
    return HttpResponseRedirect('https://www.instagram.com/hey.its.piyush')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def tictactoe(request):
    return render(request, 'tictactoe.html')

def findthebomb(request):
    return render(request, 'findthebomb.html')

def snake(request):
    return render(request, 'snakegame.html')