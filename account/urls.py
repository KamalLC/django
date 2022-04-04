from django.urls import path

from .views import register, signin, signout, profile,change_password

urlpatterns = [
    path('register/', register, name='register'),
    path('signin/', signin, name='signin'),
    path('signout/', signout, name='signout'),
    path('profile/', profile, name='profile'),
    path('change_password/', change_password, name='change_password'),
]