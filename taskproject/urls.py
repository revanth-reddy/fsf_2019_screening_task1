"""taskproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth.views import LoginView,LogoutView
from taskapp import views
urlpatterns = [
    url(r'^login/$', LoginView.as_view(template_name="registration/login.html"), name='login'),
    #url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^logout/$', LogoutView.as_view(template_name="registration/logout.html"),name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^admin/', admin.site.urls),
    path('',include('taskapp.urls')),
]
