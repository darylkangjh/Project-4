from django.contrib import admin
from .models import DMService, Discount, DAService, Category, Tag
# Register your models here.
admin.site.register(DMService)
admin.site.register(Discount)
admin.site.register(DAService)
admin.site.register(Category)
admin.site.register(Tag)
