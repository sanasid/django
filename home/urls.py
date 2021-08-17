from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('',views.index,name="home"),
    path('about',views.about,name="about"),
    path('services',views.services,name="services"),
    path('contact',views.contact,name="contact"),
    path('login',views.loginUser,name="login"),
    path('signup',views.signup,name="signup"),
    path('logout',views.logoutUser,name="logout"),
]