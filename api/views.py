import os

from rest_framework import viewsets, status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny

from api import serializers, models
from api.algorithm.pronunciationEvaluation import pronunciationService
from iboxz.settings import AUDIO_ROOT


# Create your views here.


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'id': token.user_id, 'token': token.key})


class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserMiniSerializer
    permission_classes = (AllowAny,)


class MovieViewSet(viewsets.ModelViewSet):
    queryset = models.Movie.objects.all()
    serializer_class = serializers.MovieSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    @action(detail=True, methods=['POST'])  # detail true means on a specific field
    def rate_movie(self, request, pk=None):
        if 'stars' in request.data:

            movie = models.Movie.objects.get(id=pk)
            stars = request.data['stars']
            user = request.user

            try:
                rating = models.Rating.objects.get(user=user.id, movie=movie.id)
                rating.stars = stars
                rating.save()
                serializer = serializers.RatingSerializer(rating, many=False)
                response = {'message': 'Rating Updated', 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)
            except:
                rating = models.Rating.objects.create(user=user, movie=movie, stars=stars)
                serializer = serializers.RatingSerializer(rating, many=False)
                response = {'message': 'Rating Created', 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)

        else:
            response = {'message': 'stars needed'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['POST'])  # detail true means on a specific field
    def compare_random(self, request, pk=None):
        if 'stars' in request.data:

            movie = models.Movie.objects.get(id=pk)
            stars = request.data['stars']
            user = request.user

            try:
                rating = models.Rating.objects.get(user=user.id, movie=movie.id)
                comp = rating.stars == stars
                response = {'message': 'Compared', 'result': comp}
                return Response(response, status=status.HTTP_200_OK)
            except:
                rating = models.Rating.objects.create(user=user, movie=movie, stars=stars)
                serializer = serializers.RatingSerializer(rating, many=False)
                response = {'message': 'Rating Created', 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)

        else:
            response = {'message': 'stars needed'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class RatingViewSet(viewsets.ModelViewSet):
    queryset = models.Rating.objects.all()
    serializer_class = serializers.RatingSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def update(self, request, *args, **kwargs):
        response = {'message': 'you can\'t update ratings like that'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        response = {'message': 'you can\'t create ratings like that'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)


class EvaluationJSONViewSet(viewsets.ModelViewSet):
    queryset = models.Evaluation.objects.all()
    serializer_class = serializers.EvaluationSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    @action(detail=False, methods=['GET'])
    def get_evaluation(self, request):
        user = request.user
        evalObj = models.Evaluation.objects.filter(user=user.id).last()
        serializer = serializers.EvaluationSerializer(evalObj, many=False)
        response = {'message': 'Evaluation Completed', 'result': serializer.data}
        return Response(response, status=status.HTTP_200_OK)

    @action(detail=False, methods=['POST'])
    def save_audio(self, request):
        user = request.user
        if handle_audio_file_upload(request.FILES['audio'], user.username + '.wav'):
            models.Evaluation.objects.create(user=user, audioFile=request.FILES['audio'],
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
    queryset = models.ImplementedSkillSetData.objects.all()
    serializer_class = serializers.ImplementedSkillSetDataSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class AcquiredSkillSetDataViewSet(viewsets.ModelViewSet):
    queryset = models.AcquiredSkillSetData.objects.all()
    serializer_class = serializers.AcquiredSkillSetDataSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class CandidateViewSet(viewsets.ModelViewSet):
    queryset = models.Candidate.objects.all()
    serializer_class = serializers.CandidateSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class AddressViewSet(viewsets.ModelViewSet):
    queryset = models.AddressData.objects.all()
    serializer_class = serializers.AddressSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class EducationViewSet(viewsets.ModelViewSet):
    queryset = models.Education.objects.all()
    serializer_class = serializers.EducationSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class LanguagesViewSet(viewsets.ModelViewSet):
    queryset = models.Languages.objects.all()
    serializer_class = serializers.LanguagesSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = models.Experience.objects.all()
    serializer_class = serializers.ExperienceCreateSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class RecruiterViewSet(viewsets.ModelViewSet):
    queryset = models.Recruiter.objects.all()
    serializer_class = serializers.RecruiterMiniSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class FollowViewSet(viewsets.ModelViewSet):
    queryset = models.Follow.objects.all()
    serializer_class = serializers.FollowSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    @action(detail=False, methods=['POST'])
    def follow(self, request):
        if 'follower' and 'following' in request.data:
            follower = request.data['follower']
            following = request.data['following']

            recruiter = models.User.objects.get(id=follower)
            candidate = models.User.objects.get(id=following)

            if recruiter.type == 'recruiter' and candidate.type == 'candidate':
                try:
                    followObj, created = models.Follow.objects.get_or_create(follower=recruiter, following=candidate)
                    serializer = serializers.FollowSerializer(followObj, many=False)
                    response = {'message': 'Started Following', 'result': serializer.data}
                    return Response(response, status=status.HTTP_200_OK)
                except:
                    response = {'message': 'Unable to follow'}
                    return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                response = {'message': 'Only recruiters can follow candidates'}
                return Response(response, status=status.HTTP_403_FORBIDDEN)

        else:
            response = {'message': 'Bad data provided'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['POST'])
    def unfollow(self, request):
        if 'follower' and 'following' in request.data:
            follower = request.data['follower']
            following = request.data['following']

            recruiter = models.User.objects.get(id=follower)
            candidate = models.User.objects.get(id=following)

            if recruiter.type == 'recruiter' and candidate.type == 'candidate':
                try:
                    models.Follow.objects.get(follower=recruiter, following=candidate).delete()
                    response = {'message': 'Successfully Un-followed'}
                    return Response(response, status=status.HTTP_200_OK)
                except:
                    response = {'message': 'Unable to un-follow'}
                    return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                response = {'message': 'Only recruiters can follow candidates'}
                return Response(response, status=status.HTTP_403_FORBIDDEN)

        else:
            response = {'message': 'Bad data provided'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
