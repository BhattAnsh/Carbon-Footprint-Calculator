from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path("",views.index, name="index" ),
    path("calculate/", views.calculate, name="calculate"),
    path("blog/", views.blog, name="blog"),
    path("result/", views.result, name="result"),
    path("test/", views.test, name = "test"),
    path("loginpage/", views.Login_page, name='loginpage'),
    path("signin/", views.signin_button, name='signin'),
    path('logout/', views.logout_fuc, name='logout'),
    path('login/', views.login_button, name='login'),
    path('profile/', views.userProfile, name='profile'),
    path('about/', views.about, name='about')
]

