from django.db import models
from django.conf import settings
from useraccount.models import UserBase

from django.urls import reverse
#from django.contrib.auth.models import User



class ItemManager(models.Manager):
    def get_queryset(self):
        return super(ItemManager, self).get_queryset().filter(is_active=True)







class Menu(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255,unique=True)
    image = models.ImageField(upload_to = 'images/')

    def get_absolute_url(self):
        return reverse('demo:menu_display', args=[self.slug])

    def __str__(self):
        return self.name
        


class Item(models.Model):
    menu = models.ForeignKey(Menu,related_name='item',on_delete = models.CASCADE)
    title = models.CharField(max_length=255)
    ingredients = models.TextField(blank=True)
    slug = models.SlugField(max_length=255)
    price = models.FloatField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    is_active = models.BooleanField(default=True)
    items = ItemManager()


    class Meta:
        verbose_name_plural = 'Items'
        ordering = ('-created',)

    def __str__(self):
        return self.title

class Customer(models.Model):
   user = models.OneToOneField(UserBase,null=True,blank=True,on_delete=models.CASCADE)
   name = models.CharField(max_length=200,null=True)
   email = models.CharField(max_length=200, null=True)
    

   def __str__(self):
       
       return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True,null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)
    

    def __str__(self):
        return str(self.id)

    
        


    


    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total 

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total           

class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, blank=True,null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True,null=True)
    quantity=models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.item.price * self.quantity
        return total


class ShippingAddress(models.Model):

    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True,null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True,null=True)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.address


