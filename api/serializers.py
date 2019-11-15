from rest_framework import serializers, status
from rest_framework.authtoken.models import Token

from api.models import Movie, Rating, Evaluation, Languages, AcquiredSkillSetData, ImplementedSkillSetData, UserData, \
    HighSchool, HigherSecondary, HigherSecEqDiploma, Graduation, PostGraduation, OtherDiploma, OtherQualification, \
    Education, ExperienceData, DocumentsData, PresentAddressData, PermanentAddressData, AddressData, User


class UserMiniSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
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
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {
                'write_only': True,
                'required': True
            }
        }


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = (
            'id',
            'title',
            'description',
            'number_of_ratings',
            'avg_rating'
        )


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = (
            'id',
            'stars',
            'user',
            'movie'
        )


class EvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluation
        fields = '__all__'


class LanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Languages
        fields = '__all__'


class ImplementedSkillSetDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImplementedSkillSetData
        fields = '__all__'


class AcquiredSkillSetDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcquiredSkillSetData
        fields = '__all__'


class HighSchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = HighSchool
        fields = (
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


class HigherSecondarySerializer(serializers.ModelSerializer):
    class Meta:
        model = HigherSecondary
        fields = (
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


class HigherSecEqDiplomaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HigherSecEqDiploma
        fields = (
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


class GraduationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Graduation
        fields = (
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


class PostGraduationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostGraduation
        fields = (
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


class OtherDiplomaSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherDiploma
        fields = (
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


class OtherQualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherQualification
        fields = (
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


class EducationSerializer(serializers.ModelSerializer):
    highSchool = HighSchoolSerializer(many=False)
    higherSecondary = HigherSecondarySerializer(many=False)
    higherSecEqDiploma = HigherSecEqDiplomaSerializer(many=False)
    graduation = GraduationSerializer(many=False)
    postGraduation = PostGraduationSerializer(many=False)
    otherDiploma = OtherDiplomaSerializer(many=False)
    otherQualification = OtherQualificationSerializer(many=False)

    class Meta:
        model = Education
        fields = (
            'highSchool',
            'higherSecondary',
            'higherSecEqDiploma',
            'graduation',
            'postGraduation',
            'otherDiploma',
            'otherQualification'
        )


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentsData
        fields = '__all__'


class ExperienceSerializer(serializers.ModelSerializer):
    implementedSkills = ImplementedSkillSetDataSerializer(many=True)
    acquiredSkills = AcquiredSkillSetDataSerializer(many=True)
    documents = DocumentSerializer(many=False)

    class Meta:
        model = ExperienceData
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
            'documents',
            'noticePeriod'
        )


class PresentAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = PresentAddressData
        fields = '__all__'


class PermanentAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = PermanentAddressData
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    permanentAddress = PermanentAddressSerializer(many=False)
    presentAddress = PresentAddressSerializer(many=False)

    class Meta:
        model = AddressData
        fields = (
            'permanentAddress',
            'presentAddress',
        )


class UserDataSerializer(serializers.ModelSerializer):
    education = EducationSerializer(many=False)
    experience = ExperienceSerializer(many=True)
    languages = LanguagesSerializer(many=True)
    address = AddressSerializer(many=False)

    class Meta:
        model = UserData
        fields = (
            'id',
            'user',
            'email',
            'mobile',
            'dob',
            'firstName',
            'middleName',
            'lastName',
            'fatherFirstName',
            'fatherMiddleName',
            'fatherLastName',
            'address',
            'languages',
            'education',
            'experience',
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
