from django import forms
from django.forms import widgets
from getinvolved import models

from getinvolved.models import MembershipApplicant, VolunteerApplicant


class MembershipApplicantForm(forms.ModelForm):
    class Meta:
        model = MembershipApplicant
        fields = ('__all__')
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'mobile_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mobile Number'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'reason': forms.Textarea(attrs={'class': 'mt-30 form-control'}),
        }


class VolunteerApplicantForm(forms.ModelForm):
    class Meta:
        model = VolunteerApplicant
        fields = ('__all__')
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'mobile_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mobile Number'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'project': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Project you want to volunteer'}),
            'reason': forms.Textarea(attrs={'class': 'mt-30 form-control'}),
        }
