from django.contrib import admin

from getinvolved.models import MembershipApplicant, VolunteerApplicant
# Register your models here.

admin.site.register(MembershipApplicant)
admin.site.register(VolunteerApplicant)
