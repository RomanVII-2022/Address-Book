from phonenumber_field.formfields import PhoneNumberField
from django import forms
from .models import *


class AddressCreateForm(forms.ModelForm):
    phone = PhoneNumberField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your phone number; eg +254712345678'}))
    class Meta:
        model = Address
        fields = '__all__'

        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your first name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your last name'}),
            'email':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter your email'}),
            'address':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your address'}),
        }


class AddressEditForm(forms.ModelForm):
    phone = PhoneNumberField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your phone number; eg +254712345678'}))
    class Meta:
        model = Address
        fields = '__all__'

        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your first name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your last name'}),
            'email':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter your email'}),
            'address':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your address'}),
        }