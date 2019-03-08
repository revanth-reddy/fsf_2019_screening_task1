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
    

    def del_task(self):
        """
        Checking whether Task is created with correct values
        """
        # fetching task team and user and assert task values with that
        task = Task.objects.get(title='task1temp')
        task.delete()
        #trying to fetch task1temp after delete, if it doesnot exist then None is returned
        task = Task.objects.filter(title='task1temp').first()
        self.assertEqual(task, None)


"""
Comments Test Case
"""
class CommentsTestCase(TestCase):
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
        task1 = Task.objects.get(title='task1temp')

        # Creating Comment under Task "task1temp"
        Comments.objects.create(task= task1,author = user1,comment = "sample comment by user1",created_date = created_at)
        created_at = timezone.now()
        Comments.objects.create(task= task1,author = user2,comment = "sample comment by user2",created_date = created_at)

    def test_comment(self):
        """
        Checking whether Comment is created with correct values.
        Here Task is created by user1(john) and commented by user2(bob).
        """
        # fetching task1 comments and assert task values with that
        task1 = Task.objects.get(title='task1temp')
        
        user1 = User.objects.get(username='john')
        user2 = User.objects.get(username="bob")

        com1 = Comments.objects.get(task=task1,author= user1)
        com2 = Comments.objects.get(task=task1,author= user2)
        
        # checking comment created by user1 in task1 and that of user2 in task2
        self.assertEqual(com1.comment, "sample comment by user1")
        self.assertEqual(com2.comment, "sample comment by user2")
        self.assertEqual(task1.created_by, user1)
    

    def del_comment(self):
        """
        Checking whether Comment is deleted or not
        """
        # fetching task team and user and assert task values with that
        task1 = Task.objects.get(title='task1temp')
        user1 = User.objects.get(username='john')
        
        com1 = Comments.objects.get(task=task1,author= user1)
        com1.delete()
        com1 = Comments.objects.filter(task=task1,author= user1).first()
        self.assertEqual(com1, None)


"""
Test Case for creating COmments under a Task and deleting Task, Comments of that Task should be deleted too
"""


class TaskComTestCase(TestCase):
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
        
        task1 = Task.objects.get(title='task1temp')
        
        # Creating Comment under Task "task1temp"
        Comments.objects.create(task= task1,author = user1,comment = "sample comment by user1",created_date = created_at)
        created_at = timezone.now()
        Comments.objects.create(task= task1,author = user2,comment = "sample comment by user2",created_date = created_at)


    def test_taskcomm(self):
        """
        Checking whether Comment is created with correct values
        """
        # fetching task team and user and assert task values with that
        task1 = Task.objects.get(title='task1temp')
        
        user1 = User.objects.get(username='john')
        user2 = User.objects.get(username="bob")

        com1 = Comments.objects.get(task=task1,author= user1)
        com2 = Comments.objects.get(task=task1,author= user2)
        
        # checking comment created by user1 in task1 and that of user2 in task2
        self.assertEqual(com1.comment, "sample comment by user1")
        self.assertEqual(com2.comment, "sample comment by user2")
        self.assertEqual(com1.task, task1)
        self.assertEqual(com2.task, task1)
        self.assertEqual(task1.created_by, user1)
    

    def del_taskcomm(self):
        """
        Checking whether Comment is deleted when Task is deleted
        """
        # deleting comments at first and then deleting Task
        task1 = Task.objects.get(title='task1temp')
        user1 = User.objects.get(username='john')
        user2 = User.objects.get(username="bob")
        
        comm = Comments.objects.all().filter(task=task1)
        
        for com in comm:
            com.delete()
        
        #com1 = Comments.objects.get(task=task1,author= user1)
        #com2 = Comments.objects.get(task=task1,author= user2)
        
        com1 = Comments.objects.filter(task=task1,author= user1).first()
        
        self.assertEqual(com1, None)
        #self.assertEqual(com2, None)
        
        task = Task.objects.get(title='task1temp')
        task.delete()
        task = Task.objects.filter(title='task1temp').first()
        self.assertEqual(task, None)
