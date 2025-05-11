from django import forms
from django.forms import ModelForm
from .models import account

# class signform(ModelForm):
#     class Meta:
#         model = account
#         fields = [ 'username', 'first_name', 'middle_name', 'last_name', 'gender', 'phone_number', 'nationality', 'password1', 'password1', 'email']

        # widgets = {
        #     'first_name': forms.TextInput(attrs={'class':'form-control'}),
        #     'middle_name': forms.TextInput(attrs={'class':'form-control'}),
        #     'last_name': forms.TextInput(attrs={'class':'form-control'}),
        #     'gender': forms.TextInput(attrs={'class':'form-control'}),
        #     'phone_number': forms.TextInput(attrs={'class':'form-control'}),
        #     'nationality': forms.TextInput(attrs={'class':'form-control'}),
        #     'email': forms.EmailInput(attrs={'class':'form-control'}),
        # }