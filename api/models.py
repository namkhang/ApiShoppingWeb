from django.db import models

# Create your models here.

class StoreOwner(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=100 , null=False)
    password = models.CharField(max_length=100 , null=False)
    fullname = models.CharField(max_length=100 , null=True , blank=True)
    gender = models.CharField(max_length=10 ,null=True , blank=True)
    phone = models.CharField(max_length=20 ,null=True , blank=True)

    class Meta: 
        db_table = 'store_owner'

class Store(models.Model):
    idstore = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100 , null=False)
    phone = models.CharField(max_length=100 , null=True)
    address = models.CharField(max_length=100 , null=True)
    idowner = models.ForeignKey(StoreOwner , on_delete=models.CASCADE , null=False)

    class Meta:
        db_table = 'store'         