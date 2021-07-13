from django.views.generic import View, TemplateView, FormView

from contact.models import Contact
from contact.forms import ContactForm
# Create your views here.


class ContactView(FormView):
    template_name = 'contact/contact.html'
    form_class = ContactForm
    success_url = '/contact/'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        context['contact_page'] = 'active'

        return context
