from django import forms
from .models import DMService, Discount, DAService, Category, Tag


class DMServiceForm(forms.ModelForm):
    class Meta:
        model = DMService
        fields = ('item_name', 'price', 'short_desc',
                  'long_desc', 'availability')

