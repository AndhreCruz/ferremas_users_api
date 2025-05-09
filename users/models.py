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