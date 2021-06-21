"""file_share URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from . import views



urlpatterns = [
    path("", views.Home, name="home"),
    path("plan",views.plans,name="plans"),
    path("about",views.about,name="about"),
    path("file", views.file, name="file"),
    path("views",views.views,name="views"),
    path("upload_file", views.upload_file, name="upload_file"),
    path("profile", views.profile, name="profile"),
    path("download/<int:pk>",views.download, name="download"),
    path("getfile/<int:id>",views.download_item, name="download_file"),
    path('config/', views.stripe_config),  # new
    path('create-checkout-session/', views.create_checkout_session), # new
    path('success/', views.success_pay), # new
    path('cancelled/', views.cancel_pay), # new

    
    
]
