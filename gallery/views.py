from django.views.generic import View, TemplateView

from gallery.models import Album
# Create your views here.


class GalleryView(TemplateView):
    template_name = 'gallery/gallery.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        album = Album.objects.all()

        context['gallery_page'] = 'active'
        context['albums'] = album

        return context
