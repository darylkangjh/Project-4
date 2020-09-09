from django.db import models

# Create your models here.


# Dicounts creation for all services (users may input their ) 
class discount(models.Model):
    coupon = models.CharField(blank=False, max_length=15)
    discountPrice = models.DecimalField(max_digits=10, decimal_places=3, blank=False)
    startDate = models.DateTimeField(blank=False)
    endDate = models.DateTimeField(blank=False)


    def __str__(self):
        return "Discount price is" + self.discountPrice + "from" + self.startDate + "–" + self.endDate

# !!! ...Models for digital marketing services (with no need for stock level since it is a service)
class dmService(models.Model):
    itemName = models.CharField(blank=False, max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=3, blank=False)
    shortDesc = models.CharField(blank=False, max_length=255)
    longDesc = models.TextField(blank=False) 
    availability = models.BooleanField(blank=False)
    # Take note that discounts are optional and only given to people who knows the code.
    discount = models.ForeignKey(discount, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.itemName

# !!! ...Models for digital assets (stock level required to limit the amount of digital assets sold on the page. )
class daService(models.Model):
    itemName = models.CharField(blank=False, max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=3, blank=False)
    shortDesc = models.CharField(blank=False, max_length=255)
    longDesc = models.TextField(blank=False) 
    stock = models.IntegerField(blank=False)
    availability = models.BooleanField(blank=False)
    # Take note that discounts are optional and only given to people who knows the code.
    discount = models.ForeignKey(discount, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.itemName
