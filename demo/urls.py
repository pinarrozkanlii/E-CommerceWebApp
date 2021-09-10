from django.urls import path

from . import views

app_name = 'demo'

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('item/', views.menu_display, name='menu_display'),
    path('basket/',views.basket_summary, name='basket_summary'),
    path('update_item/',views.updateItem, name='update_item'),
    path('delete_item/',views.delete_item,name='delete_item'),
    path('order/',views.orderProcess,name='order'),
]