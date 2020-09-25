from django.db import models
from digitalMarketing.models import DMService
# Create your models here.
from django.contrib.auth.models import User


# Create your models here.
class Purchase(models.Model):
    DMService_id = models.ForeignKey(DMService, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Purchase made for item#{self.DMService_id} by user#{self.user_id} on {self.purchase_date}"