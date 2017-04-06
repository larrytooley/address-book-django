from django import forms

from .models import Address 

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['first_name', 'last_name', 'phone_number',
                  'email_address', 'street_address']
        labels = {'first_name':'First Name',
                  'last_name': 'Last Name',
                  'phone_number': 'Phone Number',
                  'email_address': 'Email Address',
                  'street_address': 'Street Address' }
