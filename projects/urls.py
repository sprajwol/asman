from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from projects import views as projects_views

urlpatterns = [
    path('', projects_views.ProjectsView.as_view(), name='projects')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
