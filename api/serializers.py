from rest_framework import serializers
from api.models import StoreOwner ,Store
from django.db.models import fields


class StoreOwnerSerializes(serializers.ModelSerializer):
    class Meta: 
            model = StoreOwner
            fields = '__all__'


class StoreSerializes(serializers.ModelSerializer):
    class Meta: 
            model = Store
            fields = '__all__'