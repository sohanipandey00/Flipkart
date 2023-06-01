from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated
from customer.models import *
from customer.serializers import *
# Create your views here.
class GetCustomerView(APIView):
    def get(self,request):
        instance=Customers.objects.all()
        serializer=GetCustomerSerializer( instance,many=True)
        return Response(serializer.data)
    def post(self,request):
        params=request.data
        print("data--",params)
        serl=GetCustomerSerializer(data=params)
        serl.is_valid(raise_exception=True)
        serl.save()
        return Response({"message:":"Save Successfully"})
    
class Get_Addresses(APIView):
    def get(self,request):
        instance=Customers.objects.all()
        serializer=CustomerAddressSerializer( instance,many=True)
        return Response(serializer.data)
    
class CustomerDetailsAddressView(APIView):
    def get(self,request,pk):
        instance=Customers.objects.filter(id=pk)
        ser=CustomerDetailsAddressSerializer( instance,many=True)
        return Response(ser.data)


        
