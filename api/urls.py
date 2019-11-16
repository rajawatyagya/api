from django.urls import path
from rest_framework import routers
from django.conf.urls import include

from api import views

router = routers.DefaultRouter()

router.register('users', views.UserViewSet)
router.register('movies', views.MovieViewSet)
router.register('ratings', views.RatingViewSet)
router.register('evaluation', views.EvaluationJSONViewSet)
router.register('implementedSkillSetData', views.ImplementedSkillSetDataViewSet)
router.register('acquiredSkillSetData', views.AcquiredSkillSetDataViewSet)
router.register('candidate', views.CandidateViewSet)
router.register('recruiter', views.RecruiterViewSet)
router.register('education', views.EducationViewSet)
router.register('address', views.AddressViewSet)
router.register('languages', views.LanguagesViewSet)
router.register('experience', views.ExperienceViewSet)
router.register('activity', views.FollowViewSet)

urlpatterns = [
    path('', include(router.urls))
]
