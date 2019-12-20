import datetime
import os
from uuid import uuid4
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.postgres.fields import JSONField
from django.utils.deconstruct import deconstructible
from iboxz.settings import MEDIA_ROOT

# Create your models here.


class User(AbstractUser):
    dateOfBirth = models.DateField(
        default=datetime.date.today
    )
    middle_name = models.CharField(
        max_length=32,
        default=''
    )
    user_type = models.CharField(
        max_length=32,
        default='candidate'
    )
    REQUIRED_FIELDS = ['user_type', 'email']
    objects = UserManager()

    def __str__(self):
        return str(self.username)


@deconstructible
class UploadToPathAndRename(object):

    def __init__(self, path):
        self.sub_path = path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
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
    address_type = models.CharField(
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
        max_length=32,
        default=''
    )
    currentSalary = models.IntegerField(null=True)
    expectedSalary = models.IntegerField(null=True)
    panNumber = models.CharField(
        max_length=32,
        default=''
    )
    aadharNumber = models.IntegerField(null=True)
    gender = models.CharField(
        max_length=10,
        default=''
    )
    message = models.TextField(
        max_length=256,
        default=''
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
        max_length=128,
        default=''
    )
    twitter = models.URLField(
        max_length=128,
        default=''
    )
    linkedIn = models.URLField(
        max_length=128,
        default=''
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


class CandidateSkillSet(models.Model):
    experience = models.ForeignKey(
        Experience,
        on_delete=models.CASCADE
    )
    name = models.CharField(
        max_length=32
    )
    proficiency = models.CharField(
        max_length=32
    )
    type = models.CharField(
        max_length=32,
        default='implemented'
    )

    def __str__(self):
        return str(self.name)


class Job(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    companyName = models.CharField(
        max_length=32
    )
    title = models.CharField(
        max_length=32
    )
    type = models.CharField(
        max_length=32,
        default=''
    )
    qualification = models.CharField(
        max_length=32,
        default=''
    )
    workLocation = models.CharField(
        max_length=32
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
    scope = models.CharField(
        max_length=32
    )
    expRange = models.CharField(
        max_length=32
    )
    salaryRange = models.CharField(
        max_length=32
    )
    joining = models.CharField(
        max_length=32
    )
    docRequired = models.CharField(
        max_length=128
    )
    evaluationMandatory = models.BooleanField()
    jobDescription = models.TextField(
        max_length=1024
    )

    def __str__(self):
        return '{} - {}'.format(self.title, self.companyName)


class JobSkillSet(models.Model):
    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE
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
