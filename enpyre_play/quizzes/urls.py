from django.urls import include, path
from rest_framework import routers

from .views import QuizzAnswerViewSet, QuizzQuestionViewSet, QuizzUserAnswerViewSet, QuizzViewSet

questions_url = routers.DefaultRouter()
questions_url.register('questions', QuizzQuestionViewSet, basename='quizzes-questions')

answers_url = routers.DefaultRouter()
answers_url.register('answers', QuizzAnswerViewSet, basename='quizzes-questions-answers')

user_answers_url = routers.DefaultRouter()
user_answers_url.register(
    'user-answers', QuizzUserAnswerViewSet, basename='quizzes-questions-answers-user-answers'
)

router = routers.SimpleRouter()
router.register('', QuizzViewSet, basename='quizzes')

urlpatterns = [
    path('<int:quizz_pk>/', include(user_answers_url.urls)),
    path('<int:quizz_pk>/', include(questions_url.urls)),
    path('<int:quizz_pk>/questions/<int:question_pk>/', include(answers_url.urls)),
] + router.urls
