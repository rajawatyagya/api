import os

from rest_framework import viewsets, status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny

from api.models import Movie, Rating, Evaluation, AcquiredSkillSetData, ImplementedSkillSetData, UserData, HighSchool, \
    AddressData, PresentAddressData, PermanentAddressData
from api.serializers import MovieSerializer, RatingSerializer, UserMiniSerializer, EvaluationSerializer, \
    AcquiredSkillSetDataSerializer, ImplementedSkillSetDataSerializer, UserDataSerializer, HighSchoolSerializer, \
    AddressSerializer, PermanentAddressSerializer, PresentAddressSerializer, User

from api.algorithm.pronunciationEvaluation import pronunciationService
from iboxz.settings import AUDIO_ROOT

# Create your views here.


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'id': token.user_id, 'token': token.key})


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserMiniSerializer
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


def changeAddressData(savefrom, saveto):
    saveto.addressLine1 = savefrom.addressLine1
    saveto.addressLine2 = savefrom.addressLine2
    saveto.city = savefrom.city
    saveto.state = savefrom.state
    saveto.zipCode = savefrom.zipCode
    saveto.country = savefrom.country
    return saveto


class AddressViewSet(viewsets.ModelViewSet):
    queryset = AddressData.objects.all()
    serializer_class = AddressSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    @action(detail=True, methods=['POST'])
    def save_address(self, request, pk=None):
        if 'permanentAddress' and 'presentAddress' in request.data:
            user = User.objects.get(id=pk)
            permanentAddressData = request.data['permanentAddress']
            presentAddressData = request.data['presentAddress']

            try:
                address = AddressData.objects.get(user=user.id)
                permanentAddress = changeAddressData(permanentAddressData,
                                                     PermanentAddressData.objects.get(user=user.id))
                presentAddress = changeAddressData(presentAddressData, PresentAddressData.objects.get(user=user.id))
                address.presentAddress = presentAddress
                address.permanentAddress = permanentAddress
                serializer = AddressSerializer(address, many=False)
                response = {'message': 'Address Updated', 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)
            except:
                permanentAddress = changeAddressData(permanentAddressData,
                                                     PermanentAddressData.objects.create(user=user))
                presentAddress = changeAddressData(presentAddressData, PresentAddressData.objects.create(user=user))
                address = AddressData.objects.create(
                    user=user,
                    permanentAddress=permanentAddress,
                    presentAddress=presentAddress
                )
                serializer = AddressSerializer(address, many=False)
                response = {'message': 'Address Saved', 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)
        else:
            response = {'message': 'Address Data Needed'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class PermanentAddressViewSet(viewsets.ModelViewSet):
    queryset = PermanentAddressData.objects.all()
    serializer_class = PermanentAddressSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class PresentAddressViewSet(viewsets.ModelViewSet):
    queryset = PresentAddressData.objects.all()
    serializer_class = PresentAddressSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
