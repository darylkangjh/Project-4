from django.contrib import admin
from .models import dmService, discount, daService
# Register your models here.
admin.site.register(dmService)
admin.site.register(discount)
admin.site.register(daService)