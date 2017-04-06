from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from .models import Address
from .forms import AddressForm

# Helper functions

def check_address_owner(request, current_address):
    """ Make sure the address entry belongs to the current user."""
    if address.owner != request.user:
        raise Http404


# Create your views here.

def index(request):
    """Home page of Address Books"""
    return render(request, 'address_books/index.html')

@login_required
def addresses(request):
    """Show all addresses"""
    current_addresses = Address.objects.filter_by(owner=request.user).order_by('last_name')
    return render(request, 'address_books/addresses.html', {'addresses': current_addresses})

@login_required
def address(request, address_id):
    """Show a single address"""
    current_address = Address.objects.get(pk=address_id)

    # Check that address is owned by logged in user
    check_address_owner(request, current_address)

    return render(request, 'address_books/address.html', {'address': current_address})

@login_required
def new_address(request):
    """Add a new address"""
    if request.method != 'POST':
        # No data has been submitted, display blank form
        current_address = AddressForm()
    else:
        # Data submitted, process data
        form = AddressForm(request.POST)
        if form.is_valid():
            current_address = form.save(commit=False)
            current_address.owner = request.user
            current_address.save()
            return HttpResponseRedirect(reverse('address_books:addresses'))

    return render(request, 'address_books/new_address.html', {'form': form})

@login_required
def edit_address(request, address_id):
    """Edit an existing address"""
    current_address = Address.objects.get(id=address_id)
   # Check that address is owned by logged in user
    check_address_owner(request, current_address)

    if request.method != 'POST':
        # Fill form with curent data if no data passed
        form = AddressForm(instrance=current_address)
    else:
        # Data submitted and processed
        form = AddressForm(instance=current_address, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('address_books/address', args=current_address.id))

    return render(request, 'address_books/edit_address.html',
                  {'address': current_address, 'form': form})

def delete_address(request, address_id):
    """Delete address from address book"""
    current_address = Address.objects.get(id=address_id)

    # Check that address is owned by logged in user
    check_address_owner(request, current_address)

    current_address.delete()
    return HttpResponseRedirect(reverse('address_books:addresses'))
