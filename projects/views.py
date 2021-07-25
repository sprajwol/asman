from django.views.generic import TemplateView, DetailView

from projects.models import Project
# Create your views here.


class ProjectsView(TemplateView):
    template_name = 'projects/projects.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        if (Project.objects.all().exists()):
            project_data = Project.objects.all()
            context['project_data'] = project_data

        context['projects_page'] = 'active'

        return context


class ProjectDetailView(DetailView):
    template_name = 'projects/project_detail.html'
    model = Project

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        # print(self.kwargs['slug'])

        if (Project.objects.all().exists()):
            other_projects_data = Project.objects.all().exclude(
                slug=self.kwargs['slug'])[:5]
            context['other_projects_data'] = other_projects_data

        context['projects_page'] = 'active'
        return context
