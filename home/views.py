from django.shortcuts import render,redirect
from .forms import UserForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

def home(request):
     if request.user.is_authenticated:
          return redirect('dashboard')
     return render(request, "home.html")

def signin(request):
     if request.user.is_authenticated:
          return redirect('dashboard')
     else:
          if request.method == "POST":
               username = request.POST.get('username')
               password = request.POST.get('password1')
               user = authenticate(request, username=username, password=password)

               if user is not None:
                    login(request, user)
                    return redirect('dashboard')
               else:
                    messages.info(request, 'username or password is incorrect.')
     return render(request, "signin.html")

def signup(request):
     if request.user.is_authenticated:
          return redirect('dashboard')
     else:
          if request.method == "POST":
               form = UserForm(request.POST)
               if form.is_valid():
                    form.save()
                    username = form.cleaned_data.get("username")
                    password = form.cleaned_data.get("password1")
                    user = authenticate(username=username, password=password)
                    login(request, user)
                    return redirect("dashboard")
          else:
               form = UserForm()
          return render(request, "signup.html", {"form":form})

def signout(request):
     logout(request)
     return redirect('signin')