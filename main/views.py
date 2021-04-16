
"""
<< --------------------------------------------------------------------------------------------------------------------

        @ Author = Convertopedia
        Copyright © 2021 Convertopedia to Present
        All rights reserved

<< --------------------------------------------------------------------------------------------------------------------
"""

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages

from django.contrib.auth import get_user_model
User = get_user_model()

# ------------------------------------------------------------------------------------------------------------------------
            #Creating Views
# ------------------------------------------------------------------------------------------------------------------------

# Home view ....
def home(request):
    return render(request, 'homefinal.html')

# Login view and Login authentication ....
def auth(request):
    context = {}
    if request.method == "POST":
        email = request.POST['Email']
        password = request.POST['Password']
        user = authenticate(request, email=email, password=password)

        if user:
            login(request, user)
            if request.GET.get('next', None):
                return HttpResponseRedirect(request.GET['next'])
            return HttpResponseRedirect(reverse('main'))
        else:
            context["error"] = "Invalid Username and Password"
            return render(request, 'auth.html', context)

    else:
        return render(request, 'auth.html', context)

# Main page only auth users can only access ....
@login_required(login_url="/auth/")
def main(request):
    return render(request, 'main.html')

# Register view to create a new valid users ....
def register(request):
    if request.method == "POST":
        name = request.POST['Name']
        email = request.POST['Email']
        password = request.POST['Password']

        if User.objects.filter(email = email).exists():
            messages.error(request, f'Email id already exists')
            return redirect('auth',)
        else:
            user = User.objects.create_user(username = name, email = email, password = password)
            user.save()
            messages.success(request, f'Account created successfully')
            return redirect('auth')


# Logout to end the session ....
def logout_user(request):
    logout(request)
    return redirect('home')


def forgetpassword(request):
    return render(request, 'forgotpassword.html')

def feedback(request):
    if request.method == "POST":
        feedtext = request.POST['feedback_text']
        return redirect('main')
    return render(request, 'feedback.html')

def export(request):
    content = {}
    if request.method == 'POST':
        text = request.POST['Text']
        content['text'] = text
        return render(request, 'exportpage.html', content)
    return render(request, 'exportpage.html')