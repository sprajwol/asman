from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from projects import views as projects_views

urlpatterns = [
    path('', projects_views.ProjectsView.as_view(), name='projects'),
    path('<slug:slug>', projects_views.ProjectDetailView.as_view(),
         name='projectdetail'),
    path('ajax/', projects_views.AjaxProjectsView.as_view(), name='ajax_projects'),
    #     path('ajax/<slug:slug>', projects_views.AjaxProjectsView.as_view(),
    #          name='ajax_projects')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
