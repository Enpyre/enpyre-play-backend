from django.contrib import admin

from enpyre_play.quizzes.models import Quizz, QuizzAnswer, QuizzQuestion, QuizzUserAnswer

admin.site.register(Quizz)
admin.site.register(QuizzAnswer)
admin.site.register(QuizzQuestion)
admin.site.register(QuizzUserAnswer)
