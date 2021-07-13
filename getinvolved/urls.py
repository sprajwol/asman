from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from getinvolved import views as getinvolved_views

urlpatterns = [
    path('membership', getinvolved_views.MembershipView.as_view(), name='membership'),
    path('volunteering', getinvolved_views.VolunteeringView.as_view(),
         name='volunteering'),
    path('donation', getinvolved_views.DonationView.as_view(), name='donation'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
