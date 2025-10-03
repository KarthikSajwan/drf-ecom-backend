from django.contrib import admin
from api.models import Order, OrderItem
# Register your models here.

#When editing an Order in the admin, also show its related OrderItems
class OrderItemInLine(admin.TabularInline):
    model = OrderItem

class OrderAdmin(admin.ModelAdmin):
    inlines = [
        OrderItemInLine
    ]

admin.site.register(Order, OrderAdmin)