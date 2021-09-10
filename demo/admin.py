from django.contrib import admin

from .models import Menu, Item,Order,Customer, OrderItem,ShippingAddress

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display=['title','ingredients','slug','price','created','updated']
    prepopulated_fields = {'slug':('title',)}  

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer','date_ordered','transaction_id','complete']
    


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['item','order','quantity']

@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ['customer','order','date_added','address']

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user','name','email']
       

