from django.views.generic import TemplateView
# Create your views here.


class ProjectsView(TemplateView):
    template_name = 'projects/projects.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        context['projects_page'] = 'active'
        return context
