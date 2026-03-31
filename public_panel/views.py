from django.views import generic

class HomePageView(generic.TemplateView):
    template_name = "public-panel/index.html"

class AboutPageView(generic.TemplateView):
    template_name = "public-panel/about.html"