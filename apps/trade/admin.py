from django.contrib import admin

# Register your models here.
from apps.trade.models import ShoppingCart, OrderGoods, OrderInfo

admin.site.register(ShoppingCart)
admin.site.register(OrderGoods)
admin.site.register(OrderInfo)
