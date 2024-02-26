from django.db import models

class Warehouse(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=40)
    staff = models.ManyToManyField('Staff', blank=True, related_name='warehouses')

    def __str__(self):
        return self.name

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    description = models.TextField()
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Order(models.Model):
    products = models.ManyToManyField(Product, through='OrderItem')
    
    def total_price(self):
        total = sum(item.total_price() for item in self.order_items.all())
        return total
    
    def __str__(self):
        return f"order{self.id}"

class OrderItem(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def total_price(self):
        return self.product.price * self.quantity 
        
    

    def __str__(self):
        return f"order_item{self.id}"




class Staff(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='staff_members', blank=True, null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0) 
    is_free = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.warehouse and not self.salary:
            self.salary = 1000
        super().save(*args, **kwargs)

