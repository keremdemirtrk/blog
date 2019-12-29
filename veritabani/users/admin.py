from django.contrib import admin
from .models import Profile
from .models import *

# Register your models here.
admin.site.register(Profile)
admin.site.register(ForeignLanguageModel)
admin.site.register(IdInformationModel)
admin.site.register(ContactInformationModel)
admin.site.register(EducationInformationModel)
admin.site.register(CertificatedModel)
admin.site.register(CvModel)
admin.site.register(CompanyModel)
admin.site.register(JobNewsModel)






