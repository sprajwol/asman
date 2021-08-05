from django.views.generic import View, TemplateView

from home.models import HeroSlider
from about.models import Testimonial, Member
from projects.models import Project, ProjectCategory
# Create your views here.


class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        if (HeroSlider.objects.all().exists()):
            hero_slider_data = HeroSlider.objects.all()
        else:
            hero_slider_data = 'no_data'

        if (ProjectCategory.objects.all().exists()):
            project_cat_data = ProjectCategory.objects.all()
            context['project_cat_data'] = project_cat_data

        if (Member.objects.all().exists()):
            member_data = Member.objects.all()[:3]
        else:
            member_data = 'no_data'

        if (Testimonial.objects.all().exists()):
            testimonial_data = Testimonial.objects.all()
        else:
            testimonial_data = 'no_data'

        context['home_page'] = 'active'
        context['hero_slider_data'] = hero_slider_data
        context['testimonial_data'] = testimonial_data
        context['member_data'] = member_data
        # context['project_data'] = project_data
        return context
