from django.urls import path, re_path
from rest_framework import routers
from django.conf.urls import include, url

from api import views

router = routers.DefaultRouter()

router.register('users', views.UserViewSet)
router.register('users/address', views.AddressViewSet)
router.register('recruiter', views.RecruiterViewSet)
router.register('candidate', views.CandidateViewSet)
router.register('evaluation', views.EvaluationJSONViewSet)
router.register('education', views.EducationViewSet)
router.register('languages', views.LanguagesViewSet)
router.register('experience', views.ExperienceViewSet)
router.register('candidate_skill_set', views.CandidateSkillSetViewSet)
router.register('job', views.JobViewSet)
router.register('job_skill_set', views.JobSkillSetViewSet)
router.register('activity', views.FollowViewSet)

urlpatterns = [
    path('', include(router.urls)),
    re_path(r'^auth/', include('djoser.urls')),
    url(r'^auth/', include('djoser.urls.authtoken')),
]
