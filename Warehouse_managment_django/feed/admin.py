from django.contrib import admin
from .models import Warehouse, Product, Order, Staff, OrderItem


class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    search_fields = ('name', 'category')

admin.site.register(Warehouse, WarehouseAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'quantity', 'price', 'warehouse')
    list_filter = ('warehouse',)
    search_fields = ('name', 'description')

admin.site.register(Product,ProductAdmin)


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]

admin.site.register(Order,OrderAdmin)


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id','order', 'product', 'quantity','total_price') 
    list_filter = ('order__id', 'product')
    search_fields = ('order__id', 'product__name')

    def total_price(self, obj):
        return obj.total_price()
    total_price.short_description = 'Total Price'
admin.site.register(OrderItem,OrderItemAdmin)


class StaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'warehouse', 'salary', 'is_free')
    list_filter = ('warehouse', 'is_free')
    search_fields = ('name',)

admin.site.register(Staff,StaffAdmin)

