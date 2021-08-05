from django.http.response import JsonResponse
from django.core import serializers
from django.views.generic import TemplateView, DetailView, View

from projects.models import Project
# Create your views here.


class ProjectsView(TemplateView):
    template_name = 'projects/projects.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        if (Project.objects.all().exists()):
            past_project_data = Project.objects.all()
            context['past_project_data'] = past_project_data

        if (Project.objects.all().exists()):
            upcoming_project_data = Project.objects.all()
            context['upcoming_project_data'] = upcoming_project_data

        context['projects_page'] = 'active'

        return context


class AjaxProjectsView(View):
    def get(self, request, **kwargs):
        # print("AjaxProjectsView")
        # request should be ajax and method should be GET.
        if (self.request.is_ajax and self.request.method == 'GET'):
            category = request.GET.get('category', '')

            try:
                project_list = Project.objects.all().values()
                # print("project_list", project_list)
            except Exception as e:
                error = {"error": "No projects has yet been added."}
                error = {"error": str(e)}
                return JsonResponse(error, status=204)

            if category != '':
                project_list = project_list.filter(category__slug=category)
                # print("project_listcategory", project_list)
            # data = serializers.serialize("json", project_list)
            return JsonResponse(data={"data": list(project_list)}, status=200, safe=True)

        return JsonResponse({"error": "Invalid request method."}, status=400)


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
