from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import permissions, serializers
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.decorators import api_view , permission_classes
from .serializers import StoreOwnerSerializes , StoreSerializes
from .models import Store , StoreOwner


# Create your views here.
get_all_storeowner = openapi.Response('All store owner' , StoreOwnerSerializes)
create_storeowner = openapi.Response('Created' , StoreOwnerSerializes)
@swagger_auto_schema(operation_description='Get all store owner' , method='GET' , responses={200 : get_all_storeowner , 404 : 'Not Found'})
@swagger_auto_schema(operation_description='Create store owner' , request_body=StoreOwnerSerializes, method='POST' , responses={200 : create_storeowner , 404 : 'Not Found'})
@api_view(['GET' , 'POST'])
@permission_classes({permissions.AllowAny,})
def store_owner(request):
    if request.method == 'GET':
        obj = StoreOwner.objects.all()
        serializer = StoreOwnerSerializes(obj , many = True)
        return Response(serializer.data , status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = StoreOwnerSerializes(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)


get_detai_storeowner = openapi.Response('GET DETAIL' , StoreOwnerSerializes)
update_storeowner = openapi.Response('Updated' , StoreOwnerSerializes)
@swagger_auto_schema(operation_description='GET DETAIL STOREOWNER',method='GET'  , responses={201 : get_detai_storeowner , 404 : 'Not Found'})
@swagger_auto_schema(operation_description='UPDATED STOREOWNER',method='PUT',request_body=StoreOwnerSerializes  , responses={201 : update_storeowner , 404 : 'Not Found'})
@swagger_auto_schema(operation_description='DELETE STOREOWNER',method='DELETE'  , responses={204 : 'No Content' })
@api_view(['GET' , 'PUT' , 'DELETE'])
@permission_classes((permissions.AllowAny,))
def store_owner_detail(request , id):
        id = int(id)
        obj = StoreOwner.objects.get(id = id)
        if request.method == 'GET':     
            serializer = StoreOwnerSerializes(obj)
            return Response(serializer.data , status=status.HTTP_200_OK)
        if request.method == 'PUT':
            serializer = StoreOwnerSerializes(instance=obj , data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data , status=status.HTTP_200_OK)
        if  request.method == 'DELETE' :
            obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)



get_all_store = openapi.Response('GET ALL STORE' , StoreSerializes)
create_store = openapi.Response('Created' , StoreSerializes)
@swagger_auto_schema(operation_description='GET ALL STORE FROM DATABASE' , method='GET' , responses={200 : get_all_store , 404 : 'No Found'})
@swagger_auto_schema(operation_description='CREATE STORE' , method='POST' , request_body= StoreSerializes , responses={200 : create_store , 404 : 'No Found'})
@api_view(['GET' , 'POST'])
@permission_classes((permissions.AllowAny,))
def store(request):
    if request.method == 'GET':
        obj = Store.objects.all()
        serializer = StoreSerializes(obj, many = True)
        return Response(serializer.data ,status=status.HTTP_200_OK) 
    if request.method == 'POST' :
        serializer = StoreSerializes(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_200_OK)

get_detail_store = openapi.Response('GET DETAIL STORE', StoreSerializes)
update_store = openapi.Response('UPDATED' , StoreSerializes)
@swagger_auto_schema(operation_description='GET DETAIL STORE FROM DATABASE' , method='GET' , responses={200 : get_detail_store , 404 : 'Not Found'})
@swagger_auto_schema(operation_description='UPDATE STORE FROM DATABASE' , method='PUT' , request_body=StoreSerializes , responses={200 : update_store , 404 : 'Not Found'})
@swagger_auto_schema(operation_description='DELETE STORE FROM DATABASE' , method='DELETE',responses={204 : 'No Content'})
@api_view(['GET' , 'PUT' , 'DELETE'])
@permission_classes((permissions.AllowAny,))
def store_detail(request , id):
    id = int(id)
    obj = Store.objects.get(idstore = id)
    if request.method ==  'GET':
        serializer = StoreSerializes(obj)
        return Response(serializer.data , status=status.HTTP_200_OK)
    if request.method == 'PUT':
        serializer = StoreSerializes(instance=obj , data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_200_OK)
    if request.method == 'DELETE':
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)