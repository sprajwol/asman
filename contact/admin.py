from django.contrib import admin


from contact.models import Contact
# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'mobile_number', 'address')


admin.site.register(Contact, ContactAdmin)
