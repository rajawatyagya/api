import os

from django.contrib.auth.models import User
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.utils import json

from api.models import Movie, Rating, Evaluation, AcquiredSkillSetData, ImplementedSkillSetData, UserData, HighSchool
from api.serializers import MovieSerializer, RatingSerializer, UserSerializer, EvaluationSerializer, \
    AcquiredSkillSetDataSerializer, ImplementedSkillSetDataSerializer, UserDataSerializer, HighSchoolSerializer

from api.algorithm.pronunciationEvaluation import pronunciationService
from iboxz.settings import AUDIO_ROOT

import jsonpickle


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    @action(detail=True, methods=['POST'])  # detail true means on a specific field
    def rate_movie(self, request, pk=None):
        if 'stars' in request.data:

            movie = Movie.objects.get(id=pk)
            stars = request.data['stars']
            user = request.user

            try:
                rating = Rating.objects.get(user=user.id, movie=movie.id)
                rating.stars = stars
                rating.save()
                serializer = RatingSerializer(rating, many=False)
                response = {'message': 'Rating Updated', 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)
            except:
                rating = Rating.objects.create(user=user, movie=movie, stars=stars)
                serializer = RatingSerializer(rating, many=False)
                response = {'message': 'Rating Created', 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)

        else:
            response = {'message': 'stars needed'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['POST'])  # detail true means on a specific field
    def compare_random(self, request, pk=None):
        if 'stars' in request.data:

            movie = Movie.objects.get(id=pk)
            stars = request.data['stars']
            user = request.user

            try:
                rating = Rating.objects.get(user=user.id, movie=movie.id)
                comp = rating.stars == stars
                response = {'message': 'Compared', 'result': comp}
                return Response(response, status=status.HTTP_200_OK)
            except:
                rating = Rating.objects.create(user=user, movie=movie, stars=stars)
                serializer = RatingSerializer(rating, many=False)
                response = {'message': 'Rating Created', 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)

        else:
            response = {'message': 'stars needed'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def update(self, request, *args, **kwargs):
        response = {'message': 'you can\'t update ratings like that'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        response = {'message': 'you can\'t create ratings like that'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)


class EvaluationJSONViewSet(viewsets.ModelViewSet):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    @action(detail=False, methods=['GET'])
    def get_evaluation(self, request):
        user = request.user
        evalObj = Evaluation.objects.filter(user=user.id).last()
        serializer = EvaluationSerializer(evalObj, many=False)
        response = {'message': 'Evaluation Completed', 'result': serializer.data}
        return Response(response, status=status.HTTP_200_OK)

    @action(detail=False, methods=['POST'])
    def save_audio(self, request):
        user = request.user
        if handle_audio_file_upload(request.FILES['audio'], user.username + '.wav'):
            Evaluation.objects.create(user=user, audioFile=request.FILES['audio'],
                                      evaluationData=pronunciationService(user.username))
            response = {'message': 'Audio file saved, Evaluation started'}
            return Response(response, status=status.HTTP_201_CREATED)

    def create(self, request, *args, **kwargs):
        response = {'message': 'you can\'t create evaluation like that'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)


def handle_audio_file_upload(file, filename):
    with open(os.path.join(AUDIO_ROOT, filename), 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    return True


class ImplementedSkillSetDataViewSet(viewsets.ModelViewSet):
    queryset = ImplementedSkillSetData.objects.all()
    serializer_class = ImplementedSkillSetDataSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class AcquiredSkillSetDataViewSet(viewsets.ModelViewSet):
    queryset = AcquiredSkillSetData.objects.all()
    serializer_class = AcquiredSkillSetDataSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class UserDataViewSet(viewsets.ModelViewSet):
    queryset = UserData.objects.all()
    serializer_class = UserDataSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class HighSchoolViewSet(viewsets.ModelViewSet):
    queryset = HighSchool.objects.all()
    serializer_class = HighSchoolSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
