# Generated by Django 4.1.7 on 2023-02-20 22:16

import django.db.models.constraints
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import enpyre_play.scores.enums


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name='ID'
                    ),
                ),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('score_type', models.CharField(max_length=10)),
                ('year', models.IntegerField(null=True)),
                ('month', models.IntegerField(null=True)),
                ('week', models.IntegerField(null=True)),
            ],
            options={
                'ordering': ['score_type', '-year', 'month', 'week'],
            },
        ),
        migrations.CreateModel(
            name='UserScore',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name='ID'
                    ),
                ),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('total', models.IntegerField(default=0)),
                ('average', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('average_count', models.IntegerField(default=0)),
                (
                    'score',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='user_scores',
                        to='scores.score',
                    ),
                ),
                (
                    'user',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
            options={
                'ordering': ['-total'],
            },
        ),
        migrations.AddIndex(
            model_name='score',
            index=models.Index(
                fields=['score_type', '-year', 'month', 'week'], name='score_type_idx'
            ),
        ),
        migrations.AddConstraint(
            model_name='score',
            constraint=models.CheckConstraint(
                check=models.Q(
                    (
                        'score_type__in',
                        [
                            enpyre_play.scores.enums.ScoreTypeSet['WEEKLY'],
                            enpyre_play.scores.enums.ScoreTypeSet['MONTHLY'],
                            enpyre_play.scores.enums.ScoreTypeSet['YEARLY'],
                            enpyre_play.scores.enums.ScoreTypeSet['GLOBAL'],
                        ],
                    ),
                    models.Q(
                        models.Q(
                            ('month__isnull', False),
                            ('score_type', enpyre_play.scores.enums.ScoreTypeSet['WEEKLY']),
                            ('week__isnull', False),
                            ('year__isnull', False),
                        ),
                        models.Q(
                            ('month__isnull', False),
                            ('score_type', enpyre_play.scores.enums.ScoreTypeSet['MONTHLY']),
                            ('week__isnull', True),
                            ('year__isnull', False),
                        ),
                        models.Q(
                            ('month__isnull', True),
                            ('score_type', enpyre_play.scores.enums.ScoreTypeSet['YEARLY']),
                            ('week__isnull', True),
                            ('year__isnull', False),
                        ),
                        models.Q(
                            ('month__isnull', True),
                            ('score_type', enpyre_play.scores.enums.ScoreTypeSet['GLOBAL']),
                            ('week__isnull', True),
                            ('year__isnull', True),
                        ),
                        _connector='OR',
                    ),
                ),
                name='valid_score',
            ),
        ),
        migrations.AddConstraint(
            model_name='score',
            constraint=models.UniqueConstraint(
                deferrable=django.db.models.constraints.Deferrable['DEFERRED'],
                fields=('score_type', 'year', 'month', 'week'),
                name='unique_score',
            ),
        ),
        migrations.AddIndex(
            model_name='userscore',
            index=models.Index(fields=['-total'], name='user_total_idx'),
        ),
        migrations.AddIndex(
            model_name='userscore',
            index=models.Index(fields=['-average'], name='user_average_idx'),
        ),
    ]
