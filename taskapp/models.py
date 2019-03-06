from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.contrib.auth.models import User

class Team(models.Model):
    class Meta:
        verbose_name = _("Team")
        verbose_name_plural = _("Teams")
    title = models.CharField(_("title"), max_length=200)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='team_created', verbose_name=_('created by'),
                                   on_delete=models.SET_NULL, null=True)
    users = models.ManyToManyField(User)
    
    def __str__(self):
        return self.title

class Task(models.Model):
    class Meta:
        verbose_name = _("Task")
        verbose_name_plural = _("Tasks")
    
    STATUSES = (
        ('to-do', _('To Do')),
        ('planned', _('Planned')),
        ('in_progress', _('In Progress')),
        ('done', _('Done')),
        ('dismissed', _('Dismissed'))
    )

    title = models.CharField(_("title"), max_length=50)
    description = models.TextField(max_length=1000)
    team = models.ForeignKey(Team,on_delete=models.PROTECT)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='task_creator', verbose_name=_('task_creator'),
                                   on_delete=models.PROTECT, null=False)
    assignee = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='task_assigne', verbose_name=_('task_assigne'),
                                  on_delete=models.SET_NULL, null=True,blank=True)
    status = models.CharField(_("status"), max_length=20, choices=STATUSES,default='to-do')
    created_at = models.DateTimeField(_("created at"), auto_now_add=True, editable=False)
    last_modified = models.DateTimeField(_("last modified"), auto_now=True, editable=False)
    
    def __str__(self):
        return self.title