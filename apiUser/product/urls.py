from . import views
from django.urls import path


urlpatterns = [
    path('', views.getRoutes,name="getRoutes"),
    path('products/',views.ProductView.getProducts,name="getProducts"),  #cria o produto
    path('products/',views.ProductView.createProduct,name="createProduct"),  #pega o produto
    path('product/<str:pk>',views.ProductView.getProduct,name="getProduct"), 
    path('product/update/<str:pk>',views.ProductView.updateProduct,name="updateProduct"),  #cria uma conta de usuário
    path('product/delete/<str:pk>',views.ProductView.deleteProduct,name="deleteProduct"), # lista os usuarios

]
