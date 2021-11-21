from django.shortcuts import render
from django.views.generic import FormView, TemplateView
from django.http import HttpResponseRedirect
from django.contrib import messages

from getinvolved.models import MembershipApplicant, VolunteerApplicant
from getinvolved.forms import MembershipApplicantForm, VolunteerApplicantForm, DonationForm
# Create your views here.


class MembershipView(TemplateView):
    template_name = 'getinvolved/membership.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['getinvolved_page'] = 'active-nav-link-wrapper'
        context['membership_form'] = MembershipApplicantForm()
        return context

    def post(self, request):
        membership_form = MembershipApplicantForm(request.POST)
        print("request.POST", request.POST)

        if membership_form.is_valid():
            contact = membership_form.save()

            messages.success(
                request, 'Your membership application request message has been submitted.')
            return HttpResponseRedirect('/getinvolved/membership')


class VolunteeringView(TemplateView):
    template_name = 'getinvolved/volunteering.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['getinvolved_page'] = 'active-nav-link-wrapper'
        context['volunteering_form'] = VolunteerApplicantForm()
        return context

    def post(self, request):
        volunteering_form = VolunteerApplicantForm(request.POST)
        print("request.POST", request.POST)

        if volunteering_form.is_valid():
            contact = volunteering_form.save()

            messages.success(
                request, 'Your volunteering application request message has been submitted.')
            return HttpResponseRedirect('/getinvolved/volunteering')


class DonationView(FormView):
    template_name = 'getinvolved/donation.html'
    form_class = DonationForm
    success_url = '/donation/'

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
        # Add in a QuerySet of all the books
        context['getinvolved_page'] = 'active-nav-link-wrapper'
        context['donation_form'] = DonationForm()
        return context

    def post(self, request):
        donation_form = DonationForm(request.POST)
        print("request.POST", request.POST)

        if donation_form.is_valid():
            contact = donation_form.save()

            messages.success(
                request, 'Your donation application request message has been submitted.')
            return HttpResponseRedirect('/getinvolved/donation')
