from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),  
    path("logout/", views.logout_view, name="logout"),
    path('register/', views.register_view, name='register'), 
    path("home/", views.home_view, name="home"),
    path("societies/", views.society_list, name="society_list"),
    path("events/", views.events_list, name="events_list"),
    path("about/", views.about_view, name="about"),
    path("societies/<slug:slug>/", views.society_detail, name="society_detail"),
    path("profile/", views.profile_view, name="profile")
]