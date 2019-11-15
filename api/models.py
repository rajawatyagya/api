import collections
import datetime
from uuid import uuid4
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.postgres.fields import JSONField, ArrayField
import os

# Create your models here.
from django.utils.deconstruct import deconstructible
from rest_framework.authtoken.models import Token

from iboxz.settings import BASE_DIR, AUDIO_ROOT, MEDIA_ROOT


class User(AbstractUser):
    dateOfBirth = models.DateField(
        default=datetime.date.today
    )
    middleName = models.CharField(
        max_length=32,
        default=''
    )

    objects = UserManager()

    def __str__(self):
        return str(self.username)


@deconstructible
class UploadToPathAndRename(object):

    def __init__(self, path):
        self.sub_path = path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        # get filename
        if instance.pk:
            filename = '{}.{}'.format(instance.pk, ext)
        else:
            # set filename as random string
            filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(self.sub_path, filename)


class HighSchool(models.Model):
    courseTitle = 'High School'
    institute = models.TextField(
        max_length=250
    )
    college = models.CharField(
        max_length=32
    )
    department = models.CharField(
        max_length=32
    )
    degree = models.CharField(
        max_length=32
    )
    startDate = models.DateField()
    endDate = models.DateField()
    type = models.CharField(
        max_length=32
    )
    percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )

    def __str__(self):
        return str(self.department)


class HigherSecondary(models.Model):
    courseTitle = models.CharField(
        max_length=32
    )
    institute = models.TextField(
        max_length=250
    )
    college = models.CharField(
        max_length=32
    )
    department = models.CharField(
        max_length=32
    )
    degree = models.CharField(
        max_length=32
    )
    startDate = models.DateField()
    endDate = models.DateField()
    type = models.CharField(
        max_length=32
    )
    percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )

    def __str__(self):
        return str(self.courseTitle)


class HigherSecEqDiploma(models.Model):
    courseTitle = models.CharField(
        max_length=32
    )
    institute = models.TextField(
        max_length=250
    )
    college = models.CharField(
        max_length=32
    )
    department = models.CharField(
        max_length=32
    )
    degree = models.CharField(
        max_length=32
    )
    startDate = models.DateField()
    endDate = models.DateField()
    type = models.CharField(
        max_length=32
    )
    percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )

    def __str__(self):
        return str(self.courseTitle)


class Graduation(models.Model):
    courseTitle = models.CharField(
        max_length=32
    )
    institute = models.TextField(
        max_length=250
    )
    college = models.CharField(
        max_length=32
    )
    department = models.CharField(
        max_length=32
    )
    degree = models.CharField(
        max_length=32
    )
    startDate = models.DateField()
    endDate = models.DateField()
    type = models.CharField(
        max_length=32
    )
    percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )

    def __str__(self):
        return str(self.courseTitle)


class PostGraduation(models.Model):
    courseTitle = models.CharField(
        max_length=32
    )
    institute = models.TextField(
        max_length=250
    )
    college = models.CharField(
        max_length=32
    )
    department = models.CharField(
        max_length=32
    )
    degree = models.CharField(
        max_length=32
    )
    startDate = models.DateField()
    endDate = models.DateField()
    type = models.CharField(
        max_length=32
    )
    percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )

    def __str__(self):
        return str(self.courseTitle)


class OtherDiploma(models.Model):
    courseTitle = models.CharField(
        max_length=32
    )
    institute = models.TextField(
        max_length=250
    )
    college = models.CharField(
        max_length=32
    )
    department = models.CharField(
        max_length=32
    )
    degree = models.CharField(
        max_length=32
    )
    startDate = models.DateField()
    endDate = models.DateField()
    type = models.CharField(
        max_length=32
    )
    percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )

    def __str__(self):
        return str(self.courseTitle)


class OtherQualification(models.Model):
    courseTitle = models.CharField(
        max_length=32
    )
    institute = models.TextField(
        max_length=250
    )
    college = models.CharField(
        max_length=32
    )
    department = models.CharField(
        max_length=32
    )
    degree = models.CharField(
        max_length=32
    )
    startDate = models.DateField()
    endDate = models.DateField()
    type = models.CharField(
        max_length=32
    )
    percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )

    def __str__(self):
        return str(self.courseTitle)


class Education(models.Model):
    highSchool = models.OneToOneField(
        HighSchool,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    higherSecondary = models.OneToOneField(
        HigherSecondary,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    higherSecEqDiploma = models.OneToOneField(
        HigherSecEqDiploma,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    graduation = models.OneToOneField(
        Graduation,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    postGraduation = models.OneToOneField(
        PostGraduation,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    otherDiploma = models.OneToOneField(
        OtherDiploma,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    otherQualification = models.OneToOneField(
        OtherQualification,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    def __str__(self):
        return str(self.pk)


class PermanentAddressData(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    addressLine1 = models.TextField(
        max_length=256,
        blank=True,
        null=True
    )
    addressLine2 = models.TextField(
        max_length=256,
        blank=True,
        null=True
    )
    city = models.CharField(
        max_length=32,
        blank=True,
        null=True
    )
    state = models.CharField(
        max_length=32,
        blank=True,
        null=True
    )
    zipCode = models.IntegerField(
        blank=True,
        null=True
    )
    country = models.CharField(
        max_length=32,
        blank=True,
        null=True
    )

    def __str__(self):
        return str(self.user.username)


class PresentAddressData(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    addressLine1 = models.TextField(
        max_length=256,
        blank=True,
        null=True
    )
    addressLine2 = models.TextField(
        max_length=256,
        blank=True,
        null=True
    )
    city = models.CharField(
        max_length=32,
        blank=True,
        null=True
    )
    state = models.CharField(
        max_length=32,
        blank=True,
        null=True
    )
    zipCode = models.IntegerField(
        blank=True,
        null=True
    )
    country = models.CharField(
        max_length=32,
        blank=True,
        null=True
    )

    def __str__(self):
        return str(self.user.username)


class AddressData(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    permanentAddress = models.OneToOneField(
        PermanentAddressData,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    presentAddress = models.OneToOneField(
        PresentAddressData,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    checked = models.BooleanField(
        default=False
    )

    def __str__(self):
        return str(self.user.username)


class UserData(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    fatherFirstName = models.CharField(
        max_length=32
    )
    fatherMiddleName = models.CharField(
        max_length=32,
        blank=True,
        null=True,
        default=''
    )
    fatherLastName = models.CharField(
        max_length=32
    )
    education = models.OneToOneField(
        Education,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    address = models.OneToOneField(
        AddressData,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    currentSalary = models.IntegerField()
    expectedSalary = models.IntegerField()
    panNumber = models.CharField(
        max_length=32
    )
    aadharNumber = models.IntegerField()
    gender = models.CharField(
        max_length=10
    )
    message = models.TextField(
        max_length=256
    )
    image = models.ImageField(
        upload_to=UploadToPathAndRename(os.path.join(MEDIA_ROOT, 'profile')),
        verbose_name="Profile Picture"
    )
    resume = models.FileField(
        upload_to=UploadToPathAndRename(os.path.join(MEDIA_ROOT, 'resume')),
        verbose_name="Resume"
    )
    facebook = models.URLField(
        max_length=128
    )
    twitter = models.URLField(
        max_length=128
    )
    linkedIn = models.URLField(
        max_length=128
    )

    def __str__(self):
        return str(self.user.email)


class Movie(models.Model):
    title = models.CharField(
        max_length=32
    )
    description = models.TextField(
        max_length=360
    )

    def number_of_ratings(self):
        ratings = Rating.objects.filter(movie=self)
        return len(ratings)

    def avg_rating(self):
        summation = 0
        ratings = Rating.objects.filter(movie=self)
        for rating in ratings:
            summation += rating.stars
        if len(ratings) > 0:
            return summation / len(ratings)
        else:
            return 0

    def __str__(self):
        return str(self.title)


class Rating(models.Model):
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    stars = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )

    class Meta:
        unique_together = (('user', 'movie'),)
        index_together = (('user', 'movie'),)

    def __str__(self):
        return str(self.movie)


class Evaluation(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    evaluationData = JSONField(
        null=True,
        blank=True
    )
    audioFile = models.FileField(
        upload_to=UploadToPathAndRename(os.path.join(MEDIA_ROOT, 'audioFiles')),
        verbose_name="audioFile"
    )

    def __str__(self):
        return str(self.user.username)


class Languages(models.Model):
    userData = models.ForeignKey(
        UserData,
        on_delete=models.CASCADE,
        related_name='languages'
    )
    name = models.CharField(
        max_length=32
    )
    read = models.BooleanField()
    write = models.BooleanField()
    speak = models.BooleanField()
    native = models.BooleanField()

    def __str__(self):
        return str(self.userData.firstName)


class DocumentsData(models.Model):
    offerLetter = models.BooleanField(
        default=False
    )
    salarySlip = models.BooleanField(
        default=False
    )
    expOrRelLetter = models.BooleanField(
        default=False
    )
    resignAccept = models.BooleanField(
        default=False
    )
    promotion = models.BooleanField(
        default=False
    )


class ExperienceData(models.Model):
    userData = models.ForeignKey(
        UserData,
        on_delete=models.CASCADE,
        related_name='experience'
    )
    title = models.CharField(
        max_length=32
    )
    company = models.TextField(
        max_length=250
    )
    industry = models.CharField(
        max_length=32
    )
    department = models.CharField(
        max_length=32
    )
    functionalArea = models.CharField(
        max_length=32
    )
    role = models.CharField(
        max_length=32
    )
    scope = models.CharField(
        max_length=32
    )
    summary = models.TextField(
        max_length=524
    )
    startDate = models.DateField()
    endDate = models.DateField()
    duration = models.DurationField()
    current = models.BooleanField()
    salary = models.IntegerField()
    noticePeriod = models.DurationField()
    documents = models.OneToOneField(
        DocumentsData,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    def __str__(self):
        return str(self.userData.firstName)


class ImplementedSkillSetData(models.Model):
    experience = models.ForeignKey(
        ExperienceData,
        on_delete=models.CASCADE,
        related_name='implementedSkills'
    )
    name = models.CharField(
        max_length=32
    )
    proficiency = models.CharField(
        max_length=32
    )

    def __str__(self):
        return str(self.name)


class AcquiredSkillSetData(models.Model):
    experience = models.ForeignKey(
        ExperienceData,
        on_delete=models.CASCADE,
        related_name='acquiredSkills'
    )
    name = models.CharField(
        max_length=32
    )
    proficiency = models.CharField(
        max_length=32
    )

    def __str__(self):
        return str(self.name)
