from django.views.generic import View, TemplateView, FormView
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect

from contact.models import Contact
from contact.forms import ContactForm
# Create your views here.


class ContactView(TemplateView):
    template_name = 'contact/contact.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['contact_page'] = 'active-nav-link-wrapper'
        context['form'] = ContactForm()
        return context

    def post(self, request):
        contact_form = ContactForm(request.POST)
        print("request.POST", request.POST)

        if contact_form.is_valid():
            contact = contact_form.save()

            messages.success(
                request, 'Your contact message has been submitted.')
            return HttpResponseRedirect('/contact')
