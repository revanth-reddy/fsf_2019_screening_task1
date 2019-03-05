from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm, TeamForm, TaskForm
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
    if request.user.is_anonymous:
        return render(request,'home.html')
    teams = [team for team in Team.objects.all() if request.user in team.users.all()]
    teams_created = [team for team in Team.objects.all() if request.user == team.created_by]
    return render(request,'home.html', {'teams': teams,'teams_created': teams_created})

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

def teamedit(request, string):
    team = get_object_or_404(Team, title=string)
    if str(request.user) != str(team.created_by):
        return HttpResponse("You don't have permission to edit")
    if request.method == "POST":
        form = TeamForm(request.POST, instance=team)
        if form.is_valid():
            users = form.cleaned_data['users']
            teamtitle = request.POST.get('title')
            team.title = teamtitle
            team.users.clear()
            for user in users:
                if str(user)!=str(request.user):
                    team.users.add(user)
            team.users.add(request.user)
            team.save()
            teammates = [val for val in team.users.all() if val in team.users.all()]
            return render(request, 'teamview.html', {'team': team, 'teammates': teammates})
    else:
        form = TeamForm(instance=team)
    return render(request, 'registration/teamedit.html', {'form': form})

def teamview(request, string):
    team = get_object_or_404(Team, title=string)
    if team is None:
        return HttpResponse("Team not found")
    if str(request.user) == str(team.created_by):
        see = 1
    else:
        see = 0
    teammates = [val for val in team.users.all() if val in team.users.all()]
    return render(request, 'teamview.html', {'team': team, 'teammates': teammates, 'see': see})

@login_required
def taskreg(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            tasktitle = request.POST.get('title')
            desc = request.POST.get('description')
            teamtitle = request.POST.get('team')
            asigne = request.POST.get('assignee')
            state = request.POST.get('status')
            task = form.save(commit=False)
            task = Task.objects.create()
            task.title = tasktitle
            task.description = desc
            task.team = teamtitle
            task.assignee = asigne
            task.status = state
            task.created_by = request.user
            team.save()
            return redirect('home')
        else:
            return HttpResponse('form invalid')
    else:
        form = TaskForm(request.user)
    return render(request, 'task.html', {'form': form})