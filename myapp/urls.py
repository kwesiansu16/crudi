from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.homePageview),
    path('about/',views.aboutPageView),
]
