from django.urls import path
from apps.user.views import login, register, logout
from apps.galery.views import home

urlpatterns = [
    path('register', register, name='register'),
    path('login', login, name='login'),
    path('home', home, name='home'),
    path('logout', logout, name='logout'),
]