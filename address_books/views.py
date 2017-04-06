from django.shortcuts import render
from django.http import HttpResponse

from .models import Address

# Create your views here.

def index(response):
    """Home page of Address Books"""
    return render(response, 'address_books/index.html')

def addresses(response):
    return HttpResponse('This is the page for all addresses.')

def address(response, address_id):
    return HttpResponse('This is the page the address with an id of {}.'.format(address_id))

def new_address(response):
    return HttpResponse('This is the page for adding a new address.')

def edit_address(response, address_id):
    return HttpResponse('This is the page for editing the address with an id of {}.'.format(address_id))

def delete_address(response, address_id):
    return HttpResponse('This is the route to delete the address with an id of {}.'.format(address_id))
