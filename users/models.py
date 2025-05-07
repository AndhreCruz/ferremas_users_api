from django.db import models

class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(unique=True, max_length=50)
    
    class Meta:
        managed = False
        db_table = 'role'
        
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    rut = models.CharField(unique = True, max_length=10)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=255)
    role = models.ForeignKey(Role, models.DO_NOTHING)
    
    class Meta:
        managed = False
        db_table = 'user'
        
class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING)
    
    class Meta:
        managed = False
        db_table = 'client'

class Address(models.Model):
    address_id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, models.DO_NOTHING)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)
    address_type = models.CharField(max_length=10, blank='home', null='home')
    is_primary = models.BooleanField(default=False)
    
    class Meta:
        managed = False
        db_table = 'address'
        
class Phone(models.Model):
    phone_id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, models.DO_NOTHING)
    phone_number = models.CharField(max_length=20)
    phone_type = models.CharField(max_length=10, blank='mobile', null='mobile')
    is_primary = models.BooleanField(default=False)
    
    class Meta:
        managed = False
        db_table = 'phone'
    
class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100)
    
    class Meta:
        managed = False
        db_table = 'category'
        
class PaymentMethod(models.Model):
    method_id = models.AutoField(primary_key=True)
    method_name = models.CharField(max_length=50)
    
    class Meta:
        managed = False
        db_table = 'payment_method'
        
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, models.DO_NOTHING)
    product_name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    is_active = models.IntegerField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'product'
        
class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'cart'
        
class CartItem(models.Model):
    cart_item_id = models.AutoField(primary_key=True)
    cart = models.ForeignKey(Cart, models.DO_NOTHING)
    product = models.ForeignKey(Product, models.DO_NOTHING)
    quantity = models.IntegerField()
    
    class Meta:
        managed = False
        db_table = 'cart_item'
        
class Invoice(models.Model):
    invoice_id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, models.DO_NOTHING)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=9, blank=True, null=True)
    delivery_method = models.CharField(max_length=8)
    delivery_address = models.CharField(max_length=255, blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'invoice'
        
class InvoiceItem(models.Model):
    invoice_item_id = models.AutoField(primary_key=True)
    invoice = models.ForeignKey(Invoice, models.DO_NOTHING)
    product = models.ForeignKey(Product, models.DO_NOTHING)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        managed = False
        db_table = 'invoice_item'
        
class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    invoice = models.ForeignKey(Invoice, models.DO_NOTHING)
    method = models.ForeignKey('PaymentMethod', models.DO_NOTHING)
    confirmed = models.IntegerField(blank=True, null=True)
    paid_at = models.DateTimeField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'payment'
        
class Delivery(models.Model):
    delivery_id = models.AutoField(primary_key=True)
    invoice = models.ForeignKey(Invoice, models.DO_NOTHING)
    provider_name = models.CharField(max_length=100, blank=True, null=True)
    tracking_code = models.CharField(max_length=100, blank=True, null=True)
    delivery_status = models.CharField(max_length=10, blank=True, null=True)
    estimated_delivery_date = models.DateTimeField(blank=True, null=True)
    delivered_at = models.DateTimeField(blank=True, null=True)
    observations = models.TextField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'delivery'