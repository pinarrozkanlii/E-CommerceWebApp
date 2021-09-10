from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import *
from django.http import JsonResponse
import json
import datetime
# Create your views here.

def home_page(request):
    menu = Menu.objects.all()
    return render(request, 'demo/home.html', {'menu':menu})


def menu_display(request):
    items = Item.objects.all()
    
    return render(request, 'demo/menu_display.html',{'items':items})

def basket_summary(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer, complete=False)
        products = order.orderitem_set.all()
        basketItems=order.get_cart_items
    else:
        products=[]
        order = {'get-cart_total':0, 'get_cart_items':0, 'get_cart_items':0}
        basketItems = order['get_cart_items']

    return render(request, 'demo/summary.html',{'products':products,'order':order, 'basketItems':basketItems})

def updateItem(request):
    data = json.loads(request.body)
    itemid = data['itemid']
    action = data['action']
    quantity= data['item_qty']

    print('Action:',action)
    print('itemid: ',itemid)
    print('item_qty: ',quantity)

    customer = request.user.customer
    item = Item.objects.get(id=itemid)
    order,created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, item=item)
    basketItems=order.get_cart_items

    if action =='add':
        orderItem.quantity = quantity
        #orderItem.quantity = (orderItem.quantity + 1)
    
        #if orderItem.item in basketItems:
        #   del basketItems[itemid]
    orderItem = basketItems    
    

    #if orderItem.quantity <= str(0):
    #    orderItem.delete()        
    return JsonResponse('Item was addded', safe=False)

def delete_item(request):
    
    data = json.loads(request.body)
    itemid = data['itemid']
    action = data['action']
    print('itemid: ',itemid)
    print('action: ',action)
    customer = request.user.customer
    item = Item.objects.get(id=itemid)
    item_id=item #sonradan yaptım
    #order= Order.objects.get_object_or_404(customer=customer, complete=False)
    ordr=get_object_or_404(Order, customer=customer,complete=False) #sonradan yaptım
    #orderItem, created = OrderItem.objects.get_object_or_404(order=order, item=item)
    order_item = get_object_or_404(OrderItem, order=ordr,item=item) # sonradan yaptım
    basketItems=ordr.get_cart_items #order.get_cart_items
    

    if action =='delete':   
        if item_id in order_item:
            del basketItems[item_id]
        basketItems=order_item #orderItem 
        #orderItem.quantity = (orderItem.quantity - 1)
     
    print('Item was deleted')
    return JsonResponse('Item was deleted', safe=False) 


def orderProcess(request):
    transaction_id = datetime.datetime.now().timestamp()
    data =json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer, complete=False)
        total = float(data['form']['total'])
        order.transaction_id=transaction_id

        if total == order.get_cart_total:
            order.complete = True
        order.save()

        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            addressLine1=data['shipping']['addressLine1'],
            city=data['shipping']['city'],
            zipcode=data['shipping']['zipcode'],
            addressLine2=data['shipping']['addressLine2'],
            phoneNumber=data['shipping']['phone'],

        )    

    else:
        print('User is not logged in')    
    return JsonResponse('Payment is done', safe=False) 


        
