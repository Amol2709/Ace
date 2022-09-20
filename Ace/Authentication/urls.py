from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "Authentication"   


urlpatterns = [
    #path("", views.homepage, name="homepage"),
    path("register/", views.register_request, name="register"),
    path('login/', auth_views.LoginView.as_view(template_name='Authentication/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='Authentication/logout.html'), name='logout'),
    ]