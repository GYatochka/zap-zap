from django import forms
from django_countries.fields import CountryField
from .models import Product, Address

class ProductForm(forms.Form):
    
    name = forms.CharField(
        max_length=100, 
        min_length=5, 
        required=True, 
        label='Name:'
        )
    full_price = forms.FloatField(
        required=True, 
        label='Price:'
        )
    discount_price = forms.FloatField(
        required=False, 
        label="Discount:",
        )
    #вставити список категорій
    category = forms.ChoiceField(
        label='Category',
        choices=None)
    description = forms.Textarea(
        label='Description:',
        )
    image = forms.ImageField(
        label='Photo:',
        )
    
    def clean_price_date(self):
        price = self.cleaned_data['price']

        if price <= 0:
            raise ValueError(_('Price can\'t be below zero!'))
        
        return price
    
    def clean_discount_date(self):
        price = self.cleaned_data['discount_price']

        if price < 0:
            raise ValueError(_('Price can\'t be below zero!'))
        
        return price

    class Meta:

        model = Product
        
        fields = (
            'name',
            'price',
            'discount_price',
            'description',
            'image'
            )

        widgets = {
            'description': forms.Textarea(
                attrs={
                    'rows':'5', 
                    'cols':'5',
                    'style':'resize:none, ',
                    }
                ),
        }


class AddressForm(forms.Form):
    
    country = CountryField().formfield()
    street = forms.CharField(max_length=100, label='Street:')
    apartment = forms.CharField(max_length=30, label='Apartment:')
    zipCode = forms.CharField(max_length=20, label="ZIP:")

    class Meta:

        model = Address
        fields = (
            'country',
            'street',
            'apartment',
            'zipCode'
        )
        
        widgets = {'country': CountrySelectWidget()}