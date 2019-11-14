from django.contrib import admin
from api.models import Movie, Rating, Evaluation, ImplementedSkillSetData, AcquiredSkillSetData, UserData, Education, \
    AddressData, Languages, ExperienceData, PresentAddressData, PermanentAddressData, HighSchool, HigherSecondary, \
    HigherSecEqDiploma, Graduation, PostGraduation, OtherDiploma, OtherQualification, DocumentsData

# Register your models here.


admin.site.register(Movie)
admin.site.register(Rating)
admin.site.register(Evaluation)
admin.site.register(ImplementedSkillSetData)
admin.site.register(AcquiredSkillSetData)
admin.site.register(UserData)
admin.site.register(Education)
admin.site.register(AddressData)
admin.site.register(Languages)
admin.site.register(ExperienceData)
admin.site.register(PresentAddressData)
admin.site.register(PermanentAddressData)
admin.site.register(HighSchool)
admin.site.register(HigherSecondary)
admin.site.register(HigherSecEqDiploma)
admin.site.register(Graduation)
admin.site.register(PostGraduation)
admin.site.register(OtherDiploma)
admin.site.register(OtherQualification)
admin.site.register(DocumentsData)
