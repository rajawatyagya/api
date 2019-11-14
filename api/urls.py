from django.urls import path
from rest_framework import routers
from django.conf.urls import include

from api.views import MovieViewSet, RatingViewSet, UserViewSet, EvaluationJSONViewSet, \
    ImplementedSkillSetDataViewSet, AcquiredSkillSetDataViewSet, UserDataViewSet, HighSchoolViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('movies', MovieViewSet)
router.register('ratings', RatingViewSet)
router.register('evaluation', EvaluationJSONViewSet)
router.register('implementedSkillSetData', ImplementedSkillSetDataViewSet)
router.register('acquiredSkillSetData', AcquiredSkillSetDataViewSet)
router.register('userData', UserDataViewSet)
router.register('highSchool', HighSchoolViewSet)

urlpatterns = [
    path('', include(router.urls))
]
