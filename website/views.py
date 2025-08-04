from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "website/index.html"

class AProposView(TemplateView):
    template_name = "website/a-propos.html"

class CheckoutView(TemplateView):
    template_name = "website/checkout.html"

class CommunauteView(TemplateView):
    template_name = "website/communaute.html"

class ConfirmationView(TemplateView):
    template_name = "website/confirmation.html"

class ConsultingView(TemplateView):
    template_name = "website/consulting.html"

class ContactView(TemplateView):
    template_name = "website/contact.html"

class CoworkingView(TemplateView):
    template_name = "website/coworking.html"

class OffresView(TemplateView):
    template_name = "website/offres.html"

class SuiteView(TemplateView):
    template_name = "website/suite.html"
