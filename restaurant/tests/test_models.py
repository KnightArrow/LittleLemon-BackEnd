from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        # Create a Menu object
        item = Menu.objects.create(title="IceCream", price=100, inventory=1)
        
        # Assert individual attributes of the Menu object
        self.assertEqual(item.title, "IceCream")
        self.assertEqual(item.price, 100)
        self.assertEqual(item.inventory, 1)
        
        # Optionally, you can also check the string representation of the Menu object
        expected_string = "IceCream : 100"  # Adjust based on your __str__ method
        self.assertEqual(str(item), expected_string)

