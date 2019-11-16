from django.contrib import admin
from api import models

# Register your models here.

admin.site.register(models.User)
admin.site.register(models.Movie)
admin.site.register(models.Rating)
admin.site.register(models.Evaluation)
admin.site.register(models.ImplementedSkillSetData)
admin.site.register(models.AcquiredSkillSetData)
admin.site.register(models.Candidate)
admin.site.register(models.Education)
admin.site.register(models.AddressData)
admin.site.register(models.Languages)
admin.site.register(models.Experience)
admin.site.register(models.Follow)
