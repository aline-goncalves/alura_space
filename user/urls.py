from django.urls import path
from user.views import login, register
from galery.views import index

urlpatterns = [
    path('login', login, name='login'),
    path('register', register, name='register'),
    path('index', index, name='index'),
]
