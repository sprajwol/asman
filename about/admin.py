from django.contrib import admin

from about.models import Member, Testimonial
# Register your models here.


class MemberAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'id',)
    readonly_fields = ('created_at', 'updated_at',)
    search_fields = ('email', 'mobile_number', 'full_name')


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'id',)
    readonly_fields = ('created_at', 'updated_at',)
    search_fields = ('organization', 'full_name')


admin.site.register(Member, MemberAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
