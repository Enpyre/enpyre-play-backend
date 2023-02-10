from rest_framework import routers

from .views import QuizzViewSet

router = routers.SimpleRouter()
router.register('', QuizzViewSet, basename='quizzes')

urlpatterns = [] + router.urls
