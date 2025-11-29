from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'app1/login.html')

def bot(request):
    return render(request, 'chatbot/chatbot_page.html')

