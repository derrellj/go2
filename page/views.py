from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'page.html'
    
class ExplorePageView(TemplateView):
    template_name = 'explore.html'
    
class AboutPageView(TemplateView):
    template_name = 'about.html'
    
class ContactPageView(TemplateView):
    template_name = 'contact.html'        