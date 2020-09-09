from django.db import models

# Create your models here.


#!!! ... Categories for products sold below
class Category(models.Model):
    category = models.CharField(blank=False, max_length=255)

    def __str__(self):
        return self.category


class Tag(models.Model):
    tag = models.CharField(blank=False, max_length=255)

    def __str__(self):
        return self.tag

# !!! ...Dicounts creation for all services (users may input their ) 
class Discount(models.Model):
    coupon = models.CharField(blank=False, max_length=15)
    discount_price = models.PositiveIntegerField(blank=False)
    start_date = models.DateTimeField(blank=False)
    end_date = models.DateTimeField(blank=False)


    def __str__(self):
        return self.coupon



# !!!!!!!!!!!!!!! WITHIN THIS BOUNDS ARE PRODCT MODELS INTENDED TO BE BOUGHT BY CUSTOMERS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# !!! ...Models for digital marketing services (with no need for stock level since it is a service)
class DMService(models.Model):
    item_name = models.CharField(blank=False, max_length=255)
    price = models.PositiveIntegerField(blank=False)
    short_desc = models.CharField(blank=False, max_length=255)
    long_desc = models.TextField(blank=False) 
    availability = models.BooleanField(blank=False)
    # Take note that discounts are optional and only given to people who knows the code.
    discount = models.ForeignKey(Discount, blank=True, null=True, on_delete=models.SET_NULL)
    tag = models.ManyToManyField('tag')
    category = models.ManyToManyField('category')

    def __str__(self):
        return self.item_name

# !!! ...Models for digital assets (stock level required to limit the amount of digital assets sold on the page. )
class DAService(models.Model):
    item_name = models.CharField(blank=False, max_length=255)
    price = models.PositiveIntegerField(blank=False)
    short_desc = models.CharField(blank=False, max_length=255)
    long_desc = models.TextField(blank=False) 
    stock = models.PositiveIntegerField(blank=False)
    availability = models.BooleanField(blank=False)
    # Take note that discounts are optional and only given to people who knows the code.
    discount = models.ForeignKey(Discount, blank=True, null=True, on_delete=models.SET_NULL)
    tag = models.ManyToManyField('tag')
    category = models.ManyToManyField('category')
    
    def __str__(self):
        return self.item_name


# !!!!!!!!!!!!!!! WITHIN THIS BOUNDS ARE PRODCT MODELS INTENDED TO BE BOUGHT BY CUSTOMERS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
