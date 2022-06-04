from email import message
import re
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from accounts.forms import LoginForm, ProfileForm
from django.contrib import messages

# Create your views here.


def loginView(request):
    path = request.GET.get('next', '/')
    form = LoginForm()
    if request.user.is_authenticated:
        return redirect(reverse_lazy('profile'))

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data
            user = authenticate(request, username = user.get('username'), password = user.get('password'))
            if user:
                login(request=request, user=user)
                return redirect(path)
        messages.add_message(request,  messages.ERROR, list(form.errors.items())[0][1][0])
        

    context = {
        'login':'enable',
        'register':'disable',
        'loginForm': form
    }
    return render(request, 'login.html', context=context)

def registerView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if not authenticate(request=request, username = username, password = password):
            user = User.objects.create_user(username = username, email = email, password = password)
            # user.set_password(user.password)
            # user.save()
            return redirect(reverse_lazy('login'))
        print()


    context = {
        'login':'disable',
        'register':'enable'
    }
    return render(request, 'login.html', context=context)

@login_required
def profileView(request):
    if request.method == 'POST':
        print('post isledi')
        user = ProfileForm(request.POST)
        if user.is_valid():
            print('if isledi')
            user.save(request.user)
        else:
            print(user.errors)

    forms = ProfileForm()
    forms.initial['username'] = request.user.username
    forms.initial['first_name'] = request.user.first_name    
    forms.initial['last_name'] = request.user.last_name    
    forms.initial['email'] = request.user.email   
    
    context = {
        'forms':forms,
    }

    return render(request, 'profile.html', context = context)

def logoutView(request):
    logout(request)
    return redirect(reverse_lazy('login'))

