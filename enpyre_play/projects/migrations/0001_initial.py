# Generated by Django 4.1.5 on 2023-01-27 02:15

from django.conf import settings
from django.db import migrations, models

import enpyre_play.users.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name='ID'
                    ),
                ),
                ('title', models.CharField(help_text='Title of the project', max_length=100)),
                (
                    'description',
                    models.TextField(blank=True, help_text='Description of the project', null=True),
                ),
                ('code', models.JSONField(help_text='Code of the project', null=True)),
                ('link', models.URLField(blank=True, help_text='Link to the project', null=True)),
                ('shared', models.BooleanField(default=False, help_text='Is the project shared?')),
                ('public', models.BooleanField(default=False, help_text='Is the project public?')),
                (
                    'user',
                    models.ForeignKey(
                        on_delete=models.SET(enpyre_play.users.utils.get_sentinel_user),
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]