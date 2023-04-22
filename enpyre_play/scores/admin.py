from django.contrib import admin

from enpyre_play.scores.models import Score, UserScore

admin.site.register(Score)
admin.site.register(UserScore)
