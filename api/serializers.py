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
            'email',
            'user_type'
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


class CandidateImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Candidate
        fields = (
            'image',
        )


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


class EvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Evaluation
        fields = '__all__'


class LanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Languages
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


class CandidateSkillSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CandidateSkillSet
        fields = '__all__'


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Job
        fields = '__all__'


class JobSkillSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.JobSkillSet
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
