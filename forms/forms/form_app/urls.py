
from django.urls import path
from .views import contact_success_view,contact_view,home_view

urlpatterns = [
    path('',home_view,name='home'),
    path('/contact/',contact_view,name='contact'),
    path('/contact/success',contact_success_view,name='contact-success'),
]
