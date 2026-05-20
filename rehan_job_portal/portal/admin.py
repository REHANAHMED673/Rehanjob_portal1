from django.contrib import admin
from .models import Company, Job, ApplicantProfile, Application, Contact

admin.site.register(Company)
admin.site.register(Job)
admin.site.register(ApplicantProfile)
admin.site.register(Application)
admin.site.register(Contact)