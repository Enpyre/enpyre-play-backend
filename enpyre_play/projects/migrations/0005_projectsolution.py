# Generated by Django 4.1.7 on 2023-03-27 01:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import enpyre_play.users.utils


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0004_alter_project_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectSolution',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name='ID'
                    ),
                ),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('code', models.TextField(help_text='Solution for the project', null=True)),
                (
                    'project',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to='projects.project'
                    ),
                ),
                (
                    'user',
                    models.ForeignKey(
                        on_delete=models.SET(enpyre_play.users.utils.get_sentinel_user),
                        related_name='solutions',
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                'ordering': ['-updated_at', '-created_at'],
                'abstract': False,
            },
        ),
    ]
