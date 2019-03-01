from django.urls import path
from django.conf.urls import url,include
from taskapp import views
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from django.conf import settings
#from taskapp.views import AutocompleteJsonView
urlpatterns = [
    path('', views.home,name='home'),
    path('team/', views.teamreg,name='teamreg'),
    url(r'^ajax/users/$', views.users_list, name='users_list'),
    #path('ajax/users/', AutocompleteJsonView.as_view(),),
]