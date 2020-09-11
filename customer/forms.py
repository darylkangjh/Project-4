from django import forms
from allauth.account.forms import SignupForm
from .models import Customer


class CustomSignupForm(SignupForm):
    name = forms.CharField(required=True, max_length=255)
    company = forms.CharField(required=False)
    created_on = forms.DateTimeField(required=False)
    
    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        customer = Customer()
        customer.name = self.cleaned_data['name']
        customer.company = self.cleaned_data['company']
        customer.created_on = self.cleaned_data['created_on']
        customer.user = user
        customer.save()

        return user
