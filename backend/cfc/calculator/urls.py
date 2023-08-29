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
    path("singinbutton/", views.signin_button, name='singinbutton'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', views.login_button, name='login')
]

