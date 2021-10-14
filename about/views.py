from django.views.generic import TemplateView

from about.models import Testimonial, Member
# Create your views here.


class AboutView(TemplateView):
    template_name = 'about/about.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        if (Testimonial.objects.all().exists()):
            testimonial_data = Testimonial.objects.all()
            context['testimonial_data'] = testimonial_data

        if (Member.objects.all().exists()):
            member_data = Member.objects.all()
            context['member_data'] = member_data

        context['about_page'] = 'active'
        return context
