import datetime
from uuid import uuid4
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.postgres.fields import JSONField
from django.utils.deconstruct import deconstructible
import os

# Create your models here.
from iboxz.settings import MEDIA_ROOT


class User(AbstractUser):
    dateOfBirth = models.DateField(
        default=datetime.date.today
    )
    middle_name = models.CharField(
        max_length=32,
        default=''
    )
    type = models.CharField(
        max_length=32,
        default='candidate'
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


class Education(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    courseType = models.CharField(
        max_length=32,
        default=''
    )
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
        return str(self.courseType)


class AddressData(models.Model):
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
    type = models.CharField(
        max_length=32,
        blank=True,
        null=True,
        default='permanent'
    )

    def __str__(self):
        return str(self.user.username)


class Candidate(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    mobile = models.IntegerField(
        default=0
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
        return str(self.user.username)


class Recruiter(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    companyName = models.CharField(
        max_length=128
    )
    recruiterName = models.CharField(
        max_length=64
    )
    designation = models.CharField(
        max_length=32
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
    accountType = models.CharField(
        max_length=32
    )
    mobileNumber = models.IntegerField(null=True)
    landLine = models.IntegerField(null=True)
    website = models.URLField()
    about = models.TextField(
        max_length=256
    )

    def __str__(self):
        return str(self.companyName)


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
    user = models.ForeignKey(
        User,
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
        return str(self.user.first_name)


class Experience(models.Model):
    user = models.ForeignKey(
        User,
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
    current = models.BooleanField(
        default=False
    )
    salary = models.IntegerField()
    noticePeriod = models.DurationField()
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
    promotionLetter = models.BooleanField(
        default=False
    )

    def __str__(self):
        return str(self.user.username)


class ImplementedSkillSetData(models.Model):
    experience = models.ForeignKey(
        Experience,
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
        Experience,
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


class Follow(models.Model):
    following = models.ForeignKey(
        User,
        related_name="who_follows",
        on_delete=models.CASCADE
    )
    follower = models.ForeignKey(
        User,
        related_name="who_is_followed",
        on_delete=models.CASCADE
    )
    follow_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} following {} since {}'.format(self.follower, self.following, self.follow_time.date())
