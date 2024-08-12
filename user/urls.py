from django.urls import path
from user.views import login, register, logout
from galery.views import index

urlpatterns = [
    path('register', register, name='register'),
    path('login', login, name='login'),
    path('index', index, name='index'),
    path('logout', logout, name='logout'),
]