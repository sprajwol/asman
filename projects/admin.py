from django.contrib import admin
from django.template.loader import get_template
from django.utils.translation import gettext as _
from django_summernote.admin import SummernoteModelAdmin

from projects.models import Project, ProjectCategory
# Register your models here.


class ProjectAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)

    list_display = ('title', 'id',)
    prepopulated_fields = {'slug': ('title',)}
    fields = ('title', 'slug', 'main_image', 'image_thumb', 'date', 'location', 'category',
              'summary', 'description')

    readonly_fields = ("image_thumb",)

    def image_thumb(self, instance):
        """A (pseudo)field that returns an image thumbnail for a show photo."""
        tpl = get_template("projects/admin/project_image_thumbnail.html")
        return tpl.render({"image": instance.main_image})

    image_thumb.short_description = _("Main Image Preview")


class ProjectCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectCategory, ProjectCategoryAdmin)
