from django.db import models

class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(unique=True, max_length=50)
    
    class Meta:
        managed = False
        db_table = 'role'
        
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_run = models.CharField(unique = True, max_length=14)
    user_first_name = models.CharField(max_length=100)
    user_sec_name = models.CharField(max_length=100)
    user_first_surname = models.CharField(max_length=100)
    user_sec_surname = models.CharField(max_length=100)
    user_email = models.CharField(unique=True, max_length=100)
    user_password = models.CharField(max_length=100)
    role = models.ForeignKey(Role, on_delete=models.RESTRICT, db_column='role_id')
    
    class Meta:
        managed = False
        db_table = 'user'
        
class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    client_run = models.CharField(unique=True, max_length=14)
    client_first_name = models.CharField(max_length=100)
    client_sec_name = models.CharField(max_length=100)
    client_first_surname = models.CharField(max_length=100)
    client_sec_surname = models.CharField(max_length=100)
    client_email = models.CharField(unique=True, max_length=100)
    client_password = models.CharField(max_length=100)
    
    class Meta:
        managed = False
        db_table = 'client'

class Address(models.Model):
    ADDRESS_TYPE_CHOICES = [
        ('home', 'Home'),
        ('work', 'Work'),
        ('other', 'Other'),
    ]
    
    address_id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, db_column='client_id')
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10, null=True, blank=True)
    address_type = models.CharField(max_length=10, choices=ADDRESS_TYPE_CHOICES, default='home')
    is_primary = models.BooleanField(default=False)
    
    class Meta:
        managed = False
        db_table = 'address'  
              
class Phone(models.Model):
    PHONE_TYPE_CHOICES = [
        ('mobile', 'Mobile'),
        ('home', 'Home'),
        ('work', 'Work'),
    ]
    
    phone_id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, db_column='client_id')
    phone_number = models.CharField(max_length=20)
    phone_type = models.CharField(max_length=10, choices=PHONE_TYPE_CHOICES, default='mobile')
    is_primary = models.BooleanField(default=False)
    
    class Meta:
        managed = False
        db_table = 'phone'