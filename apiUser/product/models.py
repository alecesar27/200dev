from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Products(models.Model):
    _id= models.AutoField(primary_key=True,editable=False)    
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    name=models.CharField(max_length=150)
    image=models.ImageField(null=True,blank=True)
    brand=models.CharField(max_length=100,null=True,blank=True)
    category=models.CharField(max_length=100,null=True,blank=True)
    info=models.TextField(null=True,blank=True)
    price=models.DecimalField(max_digits=7,decimal_places=2,null=True,blank=True)
    stockcount=models.IntegerField(null=True,blank=True,default=0)
    createdAt=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name