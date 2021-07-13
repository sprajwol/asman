from django.shortcuts import render
from django.views.generic import FormView, TemplateView

from getinvolved.models import MembershipApplicant, VolunteerApplicant
from getinvolved.forms import MembershipApplicantForm, VolunteerApplicantForm
# Create your views here.


class MembershipView(FormView):
    template_name = 'getinvolved/membership.html'
    form_class = MembershipApplicantForm
    success_url = '/membership/'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        context['getinvolved_page'] = 'active'
        return context


class VolunteeringView(FormView):
    template_name = 'getinvolved/volunteering.html'
    form_class = VolunteerApplicantForm
    success_url = '/volunteering/'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        context['getinvolved_page'] = 'active'
        return context


class DonationView(TemplateView):
    template_name = 'getinvolved/donation.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        context['getinvolved_page'] = 'active'
        return context
