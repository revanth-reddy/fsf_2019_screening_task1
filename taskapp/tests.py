from django.test import TestCase
from taskapp.models import Task, Team, Comments
from django.contrib.auth.models import User
from django.utils import timezone




"""
Team Test Case
"""
class TeamTestCase(TestCase):
    def setUp(self):
        User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        User.objects.create_user('bob', 'bob@thebeatles.com', 'bobpassword')
        user1 = User.objects.get(username='john')
        user2 = User.objects.get(username="bob")
        # team created by user1
        Team.objects.create(title="team1", created_by=user1,)
        team = Team.objects.get(title="team1")
        team.users.add(user1)
        team.users.add(user2)

    def test_team(self):
        """
        Checking whether team is created with correct values
        """
        team = Team.objects.get(title="team1")
        user1 = User.objects.get(username='john')
        # checking if team is created by user1 or not
        self.assertEqual(team.created_by, user1)
        all_users = [user for user in team.users.all()]
        for user in all_users:
            print(str(user)+" is User in "+str(team))



"""
Task Test Case
"""
class TaskTestCase(TestCase):
    def setUp(self):
        # Creating Users
        User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        User.objects.create_user('bob', 'bob@thebeatles.com', 'bobpassword')
        user1 = User.objects.get(username='john')
        user2 = User.objects.get(username="bob")
        # Creating Team
        Team.objects.create(title="team1", created_by=user1,)
        team = Team.objects.get(title="team1")
        team.users.add(user1)
        team.users.add(user2)
        
        # fetching team
        team = Team.objects.get(title="team1")
        status = 'To Do'
        created_at = timezone.now()
        last_modified = timezone.now()
        
        # Creating Task
        Task.objects.create(title='task1temp',description = 'task1temp description',team = team,created_by = user1,assignee = user2,status = status,created_at = created_at,last_modified = last_modified)



    def test_team(self):
        """
        Checking whether Task is created with correct values
        """
        # fetching task team and user and assert task values with that
        task = Task.objects.get(title='task1temp')
        team = Team.objects.get(title="team1")
        user1 = User.objects.get(username='john')
        
        # checking if task is created by user1 or not
        self.assertEqual(task.created_by, user1)
        self.assertEqual(task.team, team)