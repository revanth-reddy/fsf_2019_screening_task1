from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import SignUpForm,TeamForm
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.forms.models import model_to_dict
from django.contrib.auth.models import Group, User
import simplejson as json
from .models import Team
from django.contrib.auth.decorators import login_required



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

@login_required
def users_list(request):
    username = request.GET.get('username', None)
    id = request.user.id
    user = User.objects.filter(id=id)
    all_users = User.objects.all().order_by('id').exclude(id=id)
    return JsonResponse({
            'results': [
                #{'text': str(obj.username)}
                {'id': str(obj.id), 'text': str(obj.username)}
                for obj in all_users
            ],
        })

@login_required
def teamreg(request):
    if request.method == "POST":
        form = TeamForm(request.POST)
        if form.is_valid():
            users = form.cleaned_data['users']
            teamtitle = request.POST.get('title')
            team = form.save(commit=False)
            team = Team.objects.create()
            team.title = teamtitle
            for user in users:
                team.users.add(user)
            team.users.add(request.user)
            team.created_by = request.user
            team.save()
            return redirect('home')
        else:
            return HttpResponse('form invalid')
    else:
        form = TeamForm()
    return render(request, 'registration/team.html', {'form': form})

def teamedit(request,string):
    try:
        team = Team.objects.get_object_or_404(title=string)
    except:
        return HttpResponse("Team not Found")
    return HttpResponse(a)