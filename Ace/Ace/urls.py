"""Ace URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from CoreApp.views import getAllFarmerinfo, getFarmerinfo_ID
from rest_framework.authtoken import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/get-allfarmer-info/<str:language_code>/',getAllFarmerinfo, name = 'farmer_info'),
    path('api/get-farmer-info/<int:id>/<str:language_code>/',getFarmerinfo_ID, name = 'farmer_info_id'),
    #path('home/', views.checkAPI, name='checkAPI'),
    path('authentication/',include('Authentication.urls', namespace='authentication')),
    path('',include('CoreApp.urls', namespace='app')),
    path('api-token-auth/', views.obtain_auth_token)
    
]

