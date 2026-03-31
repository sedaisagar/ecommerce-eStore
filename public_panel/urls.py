from django.urls import path

from public_panel.views import HomePageView, AboutPageView

urlpatterns = [
    path("",  HomePageView.as_view(), name="home-page"),
    path("about/",  AboutPageView.as_view(), name="about-page"),
]