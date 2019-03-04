from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Team,Task
from django.contrib.auth.models import Group, User
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ('title', 'users',)

# class TeamForm(forms.ModelForm):
#     class Meta:
#         model = Team
#         fields = ('title', 'users',)
#     # Representing the many to many related field in Team
#     users = forms.ModelMultipleChoiceField(queryset=User.objects.all())

#     # Overriding __init__ here allows us to provide initial
#     # data for 'users' field
#     def __init__(self, *args, **kwargs):
#         # Only in case we build the form from an instance
#         # (otherwise, 'users' list should be empty)
#         if kwargs.get('instance'):
#             # We get the 'initial' keyword argument or initialize it
#             # as a dict if it didn't exist.                
#             initial = kwargs.setdefault('initial', {})
#             # The widget for a ModelMultipleChoiceField expects
#             # a list of primary key for the selected data.
#             initial['users'] = [t.pk for t in kwargs['instance'].user_set.all()]

#         forms.ModelForm.__init__(self, *args, **kwargs)

#     # Overriding save allows us to process the value of 'users' field    
#     def save(self, commit=True):
#         # Get the unsave Team instance
#         instance = forms.ModelForm.save(self, False)

#         # Prepare a 'save_m2m' method for the form,
#         old_save_m2m = self.save_m2m
#         def save_m2m():
#            old_save_m2m()
#            # This is where we actually link the team with users
#            instance.user_set.clear()
#            instance.user_set.add(*self.cleaned_data['users'])
#         self.save_m2m = save_m2m

#         # Do we need to save all changes now?
#         if commit:
#             instance.save()
#             self.save_m2m()

#         return instance

