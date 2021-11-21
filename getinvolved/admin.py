from django.contrib import admin

from getinvolved.models import MembershipApplicant, VolunteerApplicant, Donation
# Register your models here.

admin.site.register(MembershipApplicant)
admin.site.register(VolunteerApplicant)
admin.site.register(Donation)
