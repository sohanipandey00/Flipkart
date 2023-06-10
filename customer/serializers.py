from rest_framework import serializers
from customer.models import *

class GetCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customers
        fields="__all__"


class CustomerAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomersAddress
        fields="__all__"


class CustomerDetailsAddressSerializer(serializers.ModelSerializer):
    customer_addresses=GetCustomerSerializer(many=True)
    
    class Meta:
        model = Customers
        fields=('first_name','last_name','mobile_number','address','age','country','dob','customer_addresses')

