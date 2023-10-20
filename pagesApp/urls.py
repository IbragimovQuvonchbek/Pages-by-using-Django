from .views import HomePageView, AboutPageView, ContactPageView, NewsPageView
from django.urls import path

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(),name='home'),
    path('news/', NewsPageView.as_view(), name='news'),
    path('contact/', ContactPageView.as_view(), name='contacts'),
]