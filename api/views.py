import os

from rest_framework import viewsets, status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from djoser import views as djoserView, conf, compat, signals

from api import serializers, models
from api.algorithm.pronunciationEvaluation import pronunciationService
from iboxz import settings


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

    @action(detail=True, methods=['POST'])
    def get_user(self, request, pk=None):
        try:
            user = models.User.objects.get(username=pk)
            serializer = serializers.UserMiniSerializer(user, many=False)
            response = {'message': 'Successful', 'result': serializer.data}
            return Response(response, status=status.HTTP_200_OK)
        except:
            response = {'message': 'User does not exist'}
            return Response(response, status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['POST'])
    def save_profile_picture(self, request, pk=None):
        user = models.User.objects.get(username=pk)
        imageFile = request.data['image']
        if imageFile and user.user_type == 'candidate':
            candidate, is_created = models.Candidate.objects.get_or_create(user=user)
            candidate.image = imageFile
            candidate.save()
            serializer = serializers.CandidateImageSerializer(candidate, many=False)
            if is_created:
                response = {'message': 'Candidate Profile Created and Profile picture saved successfully', 'result': serializer.data}
                return Response(response, status=status.HTTP_201_CREATED)
            else:
                response = {'message': 'Successful', 'result': serializer.data}
                return Response(response, status=status.HTTP_202_ACCEPTED)

        elif imageFile and user.user_type == 'client':
            response = {'message': 'Recruiter Profile, cannot save image.'}
            return Response(response, status=status.HTTP_403_FORBIDDEN)
        else:
            response = {'message': 'Not able to save profile'}
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CustomDjoserUserView(djoserView.UserViewSet):

    @action(["post"], detail=False)
    def activation(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.user
        user.is_active = True
        user.save()

        signals.user_activated.send(
            sender=self.__class__, user=user, request=self.request
        )

        if conf.settings.SEND_CONFIRMATION_EMAIL:
            context = {"user": user}
            to = [compat.get_user_email(user)]
            conf.settings.EMAIL.confirmation(self.request, context).send(to)

        return Response(status=status.HTTP_204_NO_CONTENT)


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
    with open(os.path.join(settings.AUDIO_ROOT, filename), 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    return True


class CandidateViewSet(viewsets.ModelViewSet):
    queryset = models.Candidate.objects.all()
    serializer_class = serializers.CandidateSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


def changeAddressData(savefrom, saveto):
    saveto.addressLine1 = savefrom.addressLine1
    saveto.addressLine2 = savefrom.addressLine2
    saveto.city = savefrom.city
    saveto.state = savefrom.state
    saveto.zipCode = savefrom.zipCode
    saveto.country = savefrom.country
    saveto.address_type = savefrom.address_type
    return saveto


class AddressViewSet(viewsets.ModelViewSet):
    queryset = models.AddressData.objects.all()
    serializer_class = serializers.AddressSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    @action(detail=True, methods=['POST'])
    def save_address(self, request, pk=None):
        user = models.User.objects.get(id=pk)

        if 'address_type' in request.data:
            if request.data['address_type'] == 'permanent':
                address = changeAddressData(request.data,
                                            models.AddressData.objects.get(user=user.id,
                                                                           address_type=request.data[
                                                                               'address_type']))
                serializer = serializers.AddressSerializer(address, many=False)
                response = {'message': 'Address Updated', 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)
            else:
                address = changeAddressData(request.data,
                                            models.AddressData.objects.get(user=user.id,
                                                                           address_type=request.data[
                                                                               'address_type']))
                serializer = serializers.AddressSerializer(address, many=False)
                response = {'message': 'Address Updated', 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)

        else:
            response = {'message': 'Address Data Needed'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


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


class JobSkillSetViewSet(viewsets.ModelViewSet):
    queryset = models.JobSkillSet.objects.all()
    serializer_class = serializers.JobSkillSetSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class JobViewSet(viewsets.ModelViewSet):
    queryset = models.Job.objects.all()
    serializer_class = serializers.JobSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class CandidateSkillSetViewSet(viewsets.ModelViewSet):
    queryset = models.CandidateSkillSet.objects.all()
    serializer_class = serializers.CandidateSkillSetSerializer
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
