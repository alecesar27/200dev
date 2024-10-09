import pytest # type: ignore
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .views import getRoutes, MyTokenObtainPairView, getUserProfiles, getUsers, registerUser, ActivateAccountView
from .models import  User
from .serializer import  UserSerializer

@pytest.mark.django_db
class TestViews(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user('testuser', 'testuser@example.com', 'password123')

    def test_get_routes(self):
        response = self.client.get(reverse('get_routes'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
   
    def test_my_token_obtain_pair_view(self):
        data = {'username': 'testuser', 'password': 'password123'}
        response = self.client.post(reverse('my_token_obtain_pair'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_user_profiles(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('get_user_profiles'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_users(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('get_users'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_register_user(self):
        data = {'fname': 'Test', 'lname': 'User', 'email': 'testuser@example.com', 'password': 'password123'}
        response = self.client.post(reverse('register_user'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_activate_account_view(self):
        response = self.client.get(reverse('activate_account', args=['uidb64', 'token']))
        self.assertEqual(response.status_code, status.HTTP_200_OK)