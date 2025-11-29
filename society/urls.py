"""
URL configuration for society project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path, include
# from django.conf.urls.static import static
# from django.conf import settings
# from . import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('app1.urls')), 
#      path('', views.home, name='home'),
#     path('about/', views.about, name='about'),
#      path('app1/', include('app1.urls')), 
#     path('contact/', views.contact, name='contact'),
#     path('chatbot/', include('chatbot.urls')),
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.home, name='home'),
#     path('about/', views.about, name='about'),                  #routing 
#     path('contact/', views.contact, name='contact'),
#     path('app1/', include('app1.urls')),       #transferring control to app -> app1
#     # path('login/', views.login, name='login'),
# ]

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app1.urls')),          
    path('chatbot/', include('chatbot.urls')),  
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
