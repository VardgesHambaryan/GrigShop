from django.forms import ModelForm
from .models import StayUpdated, BillingAddress, ShippingAddress, ContactUs

class StayUpdatedForm(ModelForm):
    class Meta:
        model = StayUpdated
        fields = '__all__'

class BillingAddressForm(ModelForm):
    class Meta:
        model = BillingAddress
        fields = '__all__'

class ShippingAddressForm(ModelForm):
    class Meta:
        model = ShippingAddress
        fields = '__all__'

class ContactUsForm(ModelForm):
    class Meta:
        model = ContactUs
        fields = '__all__'