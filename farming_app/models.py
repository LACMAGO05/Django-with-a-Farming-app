from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(max_length=350)
    subject = models.CharField(max_length=100)
    def __str__(self):
        return self.name

    
class account(models.Model):
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    password1= models.CharField(max_length=50)
    password2= models.CharField(max_length=50)
    email = models.EmailField()
    def __str__(self):
        return self.first_name
    
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name

class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.quantity * self.product.price
    
class verification(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    def __str__(self):
        return self.username

    

