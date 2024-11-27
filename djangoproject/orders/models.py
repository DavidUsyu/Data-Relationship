# models.py
from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)  # Customer's full name
    email = models.EmailField(unique=True)   # Email must be unique for each customer

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')  
    # Each order is linked to one customer; deleting the customer will delete related orders.
    
    order_date = models.DateTimeField(auto_now_add=True)  # Auto-set to the current date/time when the order is created.
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)  # Order's total cost

    def __str__(self):
        return f"Order {self.id} for {self.customer.name}"
