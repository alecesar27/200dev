from django.shortcuts import render,redirect

from django.contrib.auth import authenticate, login, logout

from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from .models import Products

from .serializer import  ProductsSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer # type: ignore
from rest_framework_simplejwt.views import TokenObtainPairView # type: ignore
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response



@api_view(['GET'])
def getRoutes(request):
    return Response('Hello Alex')

class ProductView(APIView):

    @api_view(['POST'])
    #@permission_classes([IsAdminUser ])
    def createProduct(request):
        serializer = ProductsSerializer(data=request.data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    @api_view(['GET'])
    @permission_classes([IsAdminUser])
    def getProducts(request):
        products=Products.objects.all()
        serializer=ProductsSerializer(products,many=True)
        return Response(serializer.data)


    @api_view(['GET'])
    @permission_classes([IsAdminUser])
    def getProduct(request,pk):
        product=Products.objects.get(_id=pk)
        serializer=ProductsSerializer(product,many=False)
        return Response(serializer.data)

    @api_view(['PUT'])
    @permission_classes([IsAdminUser])
    def updateProduct(request, pk):
        product = Products.objects.get(_id=pk)
        serializer = ProductsSerializer(product, data=request.data,many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    

    @api_view(['DELETE'])
    @permission_classes([IsAdminUser ])
    def deleteProduct(request, pk):
        try:
            product = Products.objects.get(_id=pk)
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Products.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
