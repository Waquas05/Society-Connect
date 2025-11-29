from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Society, Event, Profile, Heads
import google.generativeai as genai
from django.http import JsonResponse
from django.conf import settings

def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")   
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        login(request, user)  # log the user in immediately after registration
        return redirect("home")

    return render(request, "register.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")   # Django auth uses username
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request, "login.html", {"error": "Invalid username or password ❌"})

    return render(request, "login.html")


def home_view(request):
    societies=Society.objects.all()[:4]
    events=Event.objects.all()[:2]
    return render(request, "home.html", {"societies": societies, "events": events})


def logout_view(request):
    logout(request)
    return redirect("home")

def society_list(request):
    societies = Society.objects.all()
    return render(request, "app1/society_list.html", {"societies": societies})

def events_list(request):
    events=Event.objects.all()
    return render(request, "app1/events_list.html", {"events": events})

def about_view  (request):
    return render(request, "app1/about.html", {"about": about_view})

def society_detail(request, slug):
    society=get_object_or_404(Society, slug=slug)
    return render(request, "app1/society_detail.html", {"society": society})

def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    societies = Society.objects.all()

    if request.method == "POST":
        profile.semester = request.POST.get("semester")
        profile.course = request.POST.get("course")
        society_id = request.POST.get("society")
        profile.society = Society.objects.get(id=society_id) if society_id else None
        if request.FILES.get("photo"):
            profile.photo = request.FILES["photo"]
        profile.save()
        return redirect("home")

    return render(request, "app1/profile.html", {"profile": profile, "societies": societies})


