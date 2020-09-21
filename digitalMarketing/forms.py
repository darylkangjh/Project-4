from django import forms
from .models import DMService, Discount, DAService, Category
from cloudinary.forms import CloudinaryJsFileField

class DMServiceForm(forms.ModelForm):
    class Meta:
        model = DMService
        fields = ('item_name', 'price', 'short_desc',
                  'long_desc', 'availability', 'discount', 'tag', 'category','cover')
    cover = CloudinaryJsFileField()


class DAServiceForm(forms.ModelForm):
    class Meta:
        model = DAService
        fields = ('item_name', 'price', 'short_desc',
                  'long_desc', 'stock', 'availability',
                  'discount', 'tag', 'category','cover')
    cover = CloudinaryJsFileField()
