from django.db import models
from django.contrib.auth.models import User
import os
import random
# Create your models here.

# Blank: Empty or without content. Null: Absence of a value. MENAING NOT REQ
#TextField: Multiline text input. 
#CharField: Single-line text input, character limit.
# For this ginamit ang int for stock or rating, basically taga bilang
# Autofield = Automatically generated unique identifier field in databases.
# NOT CASCADE KASE WE WANT TO MAKE THE USER REVIEWS STAY, set null para mawala or mag blank nalng
# OnetoONefield Connects two models with unique relation.

class Product(models.Model):
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null=True)
    name = models.CharField(max_length = 200, null=True, blank=True)
    image = models.ImageField(upload_to="images/")
    brand = models.CharField(max_length = 200, null = True, blank =True)
    category = models.CharField(max_length = 200, null=True, blank= True)
    description = models.TextField(null = True, blank = True)
    rating = models.DecimalField(max_digits = 7, decimal_places = 2 
                                 , null=True, blank=True)
    numReviews = models.IntegerField(null = True, blank = True, default =0)
    price = models.DecimalField(max_digits = 7, decimal_places = 2,
                                null=True, blank = True)
    countInStock = models.IntegerField(null = True, blank= True, default = 0)
    createdAt =  models.TimeField (auto_now_add = True)
    _id = models.AutoField(primary_key=True)
    
    def __str__(self):
        return self.name
    


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null = True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null = True)
    name = models.CharField(max_length=200, null=True, blank=True)
    rating = models.DecimalField(max_digits = 7, decimal_places = 2 
                                 , null=True, blank=True)
    comment = models.TextField(null = True, blank = True)
    _id = models.AutoField(primary_key=True)

    def __str__(self):
        return str(self.rating)
    


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null = True)
    paymentMethod = models.CharField(max_length=200, null=True, blank=True)
    taxPrice = models.DecimalField(max_digits = 7, decimal_places = 2 
                                 , null=True, blank=True)
    shippingPrice = models.DecimalField(max_digits = 7, decimal_places = 2 
                                 , null=True, blank=True)
    totalPrice = models.DecimalField(max_digits = 7, decimal_places = 2 
                                 , null=True, blank=True)
    isPaid = models.BooleanField(default =True)
    paidAt = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    isDelivered = models.BooleanField(default=False)
    deliveredAt = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True)

    def __str__(self):
        return str(self.createdAt)

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null = True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null = True)
    name = models.CharField(max_length=200, null=True, blank=True)
    qty = models.IntegerField(null=True, blank=True, default=0)
    price = models.DecimalField(max_digits = 7, decimal_places = 2,
                                null=True, blank = True)
    image = models.CharField (max_length=200, null=True, blank=True)
    _id = models.AutoField(primary_key=True)

    def __str__(self):
        return str(self.name)
    


class ShippingAddress(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, null=True,
                                  blank = True)
    address = models.CharField(max_length = 200, null=True, blank=True)
    city = models.CharField(max_length = 200, null=True, blank=True)
    postalCode = models.CharField(max_length = 200, null=True, blank=True)
    shippingPrice = models.CharField(max_length = 200, null=True, blank=True)
    shippingPrice = models.DecimalField(max_digits = 7, decimal_places = 2,
                                null=True, blank = True)
    _id = models.AutoField(primary_key=True)

    def __str__(self):
        return str(self.address)
   

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_filename =random.randint(1, 2541781232)
    name, ext =get_filename_ext(filename)
    final_filename= '{new_filename}{exit}'.format(new_filename=new_filename,
                                                  ext=ext)
    return "img/{new_filename}/{final_filename}".format(new_filename=new_filename,
                                                        final_filename=final_filename)