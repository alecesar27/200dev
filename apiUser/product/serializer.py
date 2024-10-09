from rest_framework import serializers
from .models import Products
from rest_framework_simplejwt.tokens import RefreshToken # type: ignore

  
class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Products
        fields='__all__'
    
    def get__id(self,obj):
        return obj.id