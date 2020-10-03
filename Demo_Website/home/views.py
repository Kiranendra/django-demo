from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.

def homepage(request):
    return render(
                request=request,
                template_name="home/home.html",
                context={"products": Product.objects.all}
             )

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New account created {username}")
            login(request, user)
            return redirect("home:homepage")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")
            
    form = UserCreationForm
    return render(request,
                        template_name="home/register.html",
                        context={"form": form}
                      )

def logout_the_user(request):
    logout(request)
    messages.info(request, "You logged out!!!")
    return redirect("home:homepage")

def login_the_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"You are logged in as {username}")
                return redirect("home:homepage")
            else:
                for msg in form.error_messages:
                    messages.error(request, f"{msg}: {form.error_messages[msg]}")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")
                
    form = AuthenticationForm()
    return render(request,
                        "home/login.html",
                        {"form": form}
                       )
