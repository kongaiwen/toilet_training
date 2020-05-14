from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import SignUpForm, TraineeForm
from django.contrib import messages
from .models import Trainee
from django.db.models import F
import json
from django.core import serializers
# Create your views here.

def home_view(request):
    return render(request, 'toilet_training/home.html')

def signup_view(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()
        user.profile.first_name = form.cleaned_data.get('first_name')
        user.profile.last_name = form.cleaned_data.get('last_name')
        user.profile.email = form.cleaned_data.get('email')
        user.profile.user_type = form.cleaned_data.get('user_type')
        user.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'toilet_training/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request,
                  template_name = 'toilet_training/login.html',
                  context={'form':form})
                  
def logout_view(request):
    logout(request)
    return redirect('home')
    
def dashboard_view(request):
    profile = request.user.profile
    trainees = Trainee.objects.filter(trainers__user__username=request.user.username)
    return render(request=request,
           template_name='toilet_training/dashboard.html',
           context={'profile':profile,
                    'trainees':trainees,
                    })

def add_trainee_view(request):
    if request.method == 'POST':
        form = TraineeForm(request.POST)
        if form.is_valid():
            trainee = form.save()
            trainee.save()
            return redirect('dashboard')
        else:
            form = TraineeForm()
            return render(request=request,
                          template_name='toilet_training/add_trainee.html',
                          context={'form':form})
    else:
        form = TraineeForm()
        return render(request=request,
                      template_name='toilet_training/add_trainee.html',
                      context={'form':form})

def active_session_view(request, alias):
    trainee = None
    trainee_list = Trainee.objects.filter(alias=str(alias))
    if len(trainee_list) > 0:
        trainee = trainee_list[0]
    else:
        trainee = None

    return render(request,
                'toilet_training/active_session.html',
                {'trainee':trainee})

    


def trainee_data_view(request, alias):
    trainee = None
    trainee_list = Trainee.objects.filter(alias=str(alias))
    if len(trainee_list) > 0:
        trainee = trainee_list[0]
    else:
        trainee = None

    return render(request,
                'toilet_training/trainee_data.html',
                {'trainee':trainee})























