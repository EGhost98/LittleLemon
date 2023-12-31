from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from reservation.models import Menu
from reservation.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        # Add test instances of Menu model
        Menu.objects.create(Title='Pizza', Price=9.99, Inventory=1)
        Menu.objects.create(Title='Burger', Price=5.99, Inventory=1)
        # Add more test instances if needed

    def test_getall(self):
        # Create an instance of the API client
        client = APIClient()
        # Retrieve all Menu objects via the API
        url = reverse('items')
        response = client.get(url)
        # Serialize the Menu objects for comparison
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        # Assert the serialized data equals the response
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
