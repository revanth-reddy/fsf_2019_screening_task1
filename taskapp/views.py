from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import SignUpForm,TeamForm
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.forms.models import model_to_dict
import simplejson as json


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def home(request):
    return render(request,'home.html')

def teamreg(request):
    if request.method == "POST":
        form = TeamForm(request.POST)
        if form.is_valid():
            users = request.POST.get('users')
            return HttpResponse(users)
            team = form.save(commit=False)
            team.created_by = request.user
            team.save()
            return redirect('home')
        else:
            return HttpResponse('form invalid')
    else:
        form = TeamForm()
    return render(request, 'registration/team.html', {'form': form})

def users_list(request):
    username = request.GET.get('username', None)
    all_users = User.objects.all().order_by('id')
    return JsonResponse({
            'results': [
                {'id': str(obj.id), 'text': str(obj.username)}
                for obj in all_users
            ],
        })
