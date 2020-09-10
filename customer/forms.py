from django import forms 
from allauth.account.forms import SignupForm
from .models import Profile


class CustomSignupForm(SignupForm):
    name = forms.CharField(required=True, max_length=255)
    company = forms.CharField(required=False)
    created_on = forms.DateTimeField(required=False)
    
    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        profile = Profile()
        profile.name = self.cleaned_data ['name']
        profile.company = self.cleaned_data ['company']
        profile.created_on = self.cleaned_data ['created_on']
        profile.user = user
        profile.save()

        return user



