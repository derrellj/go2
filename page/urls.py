from django.urls import path
from .views import HomePageView, ExplorePageView, ContactPageView, AboutPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('explore/', ExplorePageView.as_view(), name='explore'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('about/', AboutPageView.as_view(), name='about'),  

]
