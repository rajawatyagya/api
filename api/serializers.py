from rest_framework import serializers, status
from rest_framework.authtoken.models import Token

from api import models


class UserMiniSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = (
            'id',
            'username',
            'password',  # password needs to be hashed
        )
        extra_kwargs = {
            'password': {
                'write_only': True,
                'required': True
            }
        }

    def create(self, validated_data):
        user = models.User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'
        extra_kwargs = {
            'password': {
                'write_only': True,
                'required': True
            }
        }


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Movie
        fields = (
            'id',
            'title',
            'description',
            'number_of_ratings',
            'avg_rating'
        )


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Rating
        fields = (
            'id',
            'stars',
            'user',
            'movie'
        )


class EvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Evaluation
        fields = '__all__'


class LanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Languages
        fields = '__all__'


class ImplementedSkillSetDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ImplementedSkillSetData
        fields = '__all__'


class AcquiredSkillSetDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AcquiredSkillSetData
        fields = '__all__'


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Education
        fields = (
            'id',
            'user',
            'courseType',
            'courseTitle',
            'institute',
            'college',
            'department',
            'degree',
            'startDate',
            'endDate',
            'type',
            'percentage'
        )


class ExperienceCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Experience
        fields = '__all__'


class ExperienceSerializer(serializers.ModelSerializer):
    implementedSkills = ImplementedSkillSetDataSerializer(many=True)
    acquiredSkills = AcquiredSkillSetDataSerializer(many=True)

    class Meta:
        model = models.Experience
        fields = (
            'id',
            'title',
            'company',
            'industry',
            'department',
            'functionalArea',
            'role',
            'scope',
            'implementedSkills',
            'acquiredSkills',
            'summary',
            'startDate',
            'endDate',
            'duration',
            'current',
            'salary',
            'noticePeriod',
            'offerLetter',
            'salarySlip',
            'expOrRelLetter',
            'resignAccept',
            'promotionLetter'
        )


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AddressData
        fields = '__all__'


class CandidateSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Candidate
        fields = (
            'id',
            'user',
            'mobile',
            'fatherFirstName',
            'fatherMiddleName',
            'fatherLastName',
            'currentSalary',
            'expectedSalary',
            'panNumber',
            'aadharNumber',
            'gender',
            'message',
            'image',
            'resume',
            'facebook',
            'twitter',
            'linkedIn'
        )


class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Follow
        fields = '__all__'


class RecruiterMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Recruiter
        fields = (
            'id',
            'user',
            'companyName',
            'recruiterName',
            'website'
        )


class RecruiterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Recruiter
        fields = '__all__'
