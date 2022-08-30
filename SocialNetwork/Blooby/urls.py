from django.urls import path
from Blooby.views import home

urlpatterns = [
    path('', home, name='home'),
]