from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages

from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.

def home(request):
    return render(request, 'home.html')


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


@login_required(login_url="/auth/")
def main(request):
    return render(request, 'main.html')

def register(request):
    if request.method == "POST":
        name = request.POST['Name']
        email = request.POST['Email']
        password = request.POST['Password']

        if User.objects.filter(email = email).exists():
            messages.error(request, f'The Emailid {email} already exists')
            return redirect('auth',)
        else:
            user = User.objects.create_user(username = name, email = email, password = password)
            user.save()
            messages.success(request, f'Account created successfully, try with login')
            return redirect('auth',)



def logout_user(request):
    if request.method == "POST":
        logout(request)
        return HttpResponseRedirect(reverse('home'))
