from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm,UserChangeForm
# Create your views here.
from .forms import SignUpForm,CustomUserChangeForm
from django.contrib.auth import login,logout, authenticate,update_session_auth_hash
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #return render(request, 'account/register_done.html')
            return redirect('/signin')
    else:
        form = SignUpForm()
    return render(request, 'account/register.html', {'form': form})
    
def signin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request = request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('/profile')
            else:
                messages.success(request, 'Username and Password didn\'t match!!') 
                return redirect('/signin')
        else:
            form = AuthenticationForm()
            return render(request, 'account/signin.html', {'form': form})
    else:
        return redirect('/profile')

def profile(request):
    name = request.user
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CustomUserChangeForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                return redirect('/profile')
        else:
            form = CustomUserChangeForm(instance=request.user)
            return render(request, 'account/profile.html', {'form': form, 'name': name})
    else:
        return redirect('/signin')


def signout(request):
    logout(request)
    return redirect('/signin')



def change_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)
                return redirect('/profile')
        else:
            form = PasswordChangeForm(user=request.user)
            return render(request, 'account/change_password.html', {'form': form, 'name': request.user})
    else:
        return redirect('/signin')