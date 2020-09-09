from django.contrib import admin
from .models import dmService, discount, daService, category, tag
# Register your models here.
admin.site.register(dmService)
admin.site.register(discount)
admin.site.register(daService)
admin.site.register(category)
admin.site.register(tag)