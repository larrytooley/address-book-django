"""Defines URL patterns for address_books."""
from django.conf.urls import url
from . import views

urlpatterns = [
    # Home page
    url(r'^$', views.index, name='index'),
    # Show all addresses.
    url(r'^addresses/$', views.addresses, name='addresses'),
    # Detail page for a single address
    url(r'^address/(?P<address_id>\d+)/$', views.address, name='address'),
    # Page for adding a new address
    url(r'^new_address/$', views.new_address, name='new_address'),
    # Page for editing an address
    url(r'^edit_address/(?P<address_id>\d+)/$', views.edit_address, name='edit_address'),
    # Routing for deleting an address
    url(r'^delete_address/(?P<address_id>\d+)/$', views.delete_address, name='delete_address'),
]