# Generated by Django 3.0 on 2019-12-18 18:54

import api.models
import datetime
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('dateOfBirth', models.DateField(default=datetime.date.today)),
                ('middle_name', models.CharField(default='', max_length=32)),
                ('user_type', models.CharField(default='candidate', max_length=32)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyName', models.CharField(max_length=32)),
                ('title', models.CharField(max_length=32)),
                ('type', models.CharField(default='', max_length=32)),
                ('qualification', models.CharField(default='', max_length=32)),
                ('workLocation', models.CharField(max_length=32)),
                ('designation', models.CharField(max_length=32)),
                ('industry', models.CharField(max_length=32)),
                ('department', models.CharField(max_length=32)),
                ('functionalArea', models.CharField(max_length=32)),
                ('role', models.CharField(max_length=32)),
                ('scope', models.CharField(max_length=32)),
                ('expRange', models.CharField(max_length=32)),
                ('salaryRange', models.CharField(max_length=32)),
                ('joining', models.CharField(max_length=32)),
                ('docRequired', models.CharField(max_length=128)),
                ('evaluationMandatory', models.BooleanField()),
                ('jobDescription', models.TextField(max_length=1024)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Recruiter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyName', models.CharField(max_length=128)),
                ('recruiterName', models.CharField(max_length=64)),
                ('designation', models.CharField(max_length=32)),
                ('industry', models.CharField(max_length=32)),
                ('department', models.CharField(max_length=32)),
                ('functionalArea', models.CharField(max_length=32)),
                ('role', models.CharField(max_length=32)),
                ('accountType', models.CharField(max_length=32)),
                ('mobileNumber', models.IntegerField(null=True)),
                ('landLine', models.IntegerField(null=True)),
                ('website', models.URLField()),
                ('about', models.TextField(max_length=256)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('read', models.BooleanField()),
                ('write', models.BooleanField()),
                ('speak', models.BooleanField()),
                ('native', models.BooleanField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='languages', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JobSkillSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('proficiency', models.CharField(max_length=32)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Job')),
            ],
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follow_time', models.DateTimeField(auto_now=True)),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='who_is_followed', to=settings.AUTH_USER_MODEL)),
                ('following', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='who_follows', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('company', models.TextField(max_length=250)),
                ('industry', models.CharField(max_length=32)),
                ('department', models.CharField(max_length=32)),
                ('functionalArea', models.CharField(max_length=32)),
                ('role', models.CharField(max_length=32)),
                ('scope', models.CharField(max_length=32)),
                ('summary', models.TextField(max_length=524)),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
                ('duration', models.DurationField()),
                ('current', models.BooleanField(default=False)),
                ('salary', models.IntegerField()),
                ('noticePeriod', models.DurationField()),
                ('offerLetter', models.BooleanField(default=False)),
                ('salarySlip', models.BooleanField(default=False)),
                ('expOrRelLetter', models.BooleanField(default=False)),
                ('resignAccept', models.BooleanField(default=False)),
                ('promotionLetter', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experience', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evaluationData', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('audioFile', models.FileField(upload_to=api.models.UploadToPathAndRename('/home/chigga/Documents/Code/DjangoApi/media/audioFiles'), verbose_name='audioFile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseType', models.CharField(default='', max_length=32)),
                ('courseTitle', models.CharField(max_length=32)),
                ('institute', models.TextField(max_length=250)),
                ('college', models.CharField(max_length=32)),
                ('department', models.CharField(max_length=32)),
                ('degree', models.CharField(max_length=32)),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
                ('type', models.CharField(max_length=32)),
                ('percentage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CandidateSkillSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('proficiency', models.CharField(max_length=32)),
                ('type', models.CharField(default='implemented', max_length=32)),
                ('experience', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Experience')),
            ],
        ),
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.IntegerField(default=0)),
                ('fatherFirstName', models.CharField(max_length=32)),
                ('fatherMiddleName', models.CharField(blank=True, default='', max_length=32, null=True)),
                ('fatherLastName', models.CharField(default='', max_length=32)),
                ('currentSalary', models.IntegerField(null=True)),
                ('expectedSalary', models.IntegerField(null=True)),
                ('panNumber', models.CharField(default='', max_length=32)),
                ('aadharNumber', models.IntegerField(null=True)),
                ('gender', models.CharField(default='', max_length=10)),
                ('message', models.TextField(default='', max_length=256)),
                ('image', models.ImageField(upload_to=api.models.UploadToPathAndRename('/home/chigga/Documents/Code/DjangoApi/media/profile'), verbose_name='Profile Picture')),
                ('resume', models.FileField(upload_to=api.models.UploadToPathAndRename('/home/chigga/Documents/Code/DjangoApi/media/resume'), verbose_name='Resume')),
                ('facebook', models.URLField(default='', max_length=128)),
                ('twitter', models.URLField(default='', max_length=128)),
                ('linkedIn', models.URLField(default='', max_length=128)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AddressData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addressLine1', models.TextField(blank=True, max_length=256, null=True)),
                ('addressLine2', models.TextField(blank=True, max_length=256, null=True)),
                ('city', models.CharField(blank=True, max_length=32, null=True)),
                ('state', models.CharField(blank=True, max_length=32, null=True)),
                ('zipCode', models.IntegerField(blank=True, null=True)),
                ('country', models.CharField(blank=True, max_length=32, null=True)),
                ('type', models.CharField(blank=True, default='permanent', max_length=32, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
