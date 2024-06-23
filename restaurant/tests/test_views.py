from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from ..models import Menu
from ..serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu1 = Menu.objects.create(title='Pizza', price=10.99, category='Main Course')
        self.menu2 = Menu.objects.create(title='Salad', price=5.99, category='Appetizer')

    def test_getall(self):
        url = reverse('menu-list')  # Assuming 'menu-list' is the view name for listing all Menu objects
        response = self.client.get(url)
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
