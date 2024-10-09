from . import views
from django.urls import path
from rest_framework_simplejwt.views import ( # type: ignore
    TokenObtainPairView
)

urlpatterns = [
    path('', views.getRoutes,name="getRoutes"),
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'), #rota que cria o token
    path('users/profile/',views.getUserProfiles,name="getUserProfiles"),  #pega o token do usuário criado
    path('users/register/',views.registerUser,name="register"),  #cria uma conta de usuário
    path('users/',views.getUsers,name="getUsers"), # lista os usuarios
    path('user/<str:pk>',views.getUser,name="getUser"), # lista um usuário específico 
    path('activate/<uidb64>/<token>',views.ActivateAccountView.as_view(),name='activate'),# gera un token, cria um link de ativação e envia por email
]
