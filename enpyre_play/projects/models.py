from django.contrib.auth import get_user_model
from django.db import models

from enpyre_play.users.utils import get_sentinel_user


class Project(models.Model):
    title = models.CharField(max_length=100, help_text='Title of the project')
    description = models.TextField(null=True, blank=True, help_text='Description of the project')
    code = models.JSONField(null=True, blank=False, help_text='Code of the project')
    link = models.URLField(null=True, blank=True, unique=True, help_text='Link to the project')
    shared = models.BooleanField(default=False, help_text='Is the project shared?')
    public = models.BooleanField(default=False, help_text='Is the project public?')

    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET(get_sentinel_user),
    )
