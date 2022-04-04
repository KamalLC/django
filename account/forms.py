from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm



class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class CustomUserChangeForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ('username','first_name','last_name', 'email','date_joined','last_login')
        labels = {
            'username': 'Username',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'date_joined': 'Date Joined',
            'last_login': 'Last Login',
        }