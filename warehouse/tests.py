from django.test import TestCase
from .models import Warehouse
# Create your tests here.

class WarehouseTestCase(TestCase):
    def setUp(self):
        Warehouse.objects.create(name = '1234567890',
                                email = 'prs')

    
    def test_warehouse(self):
        name = Warehouse.objects.get(name = '1234567890')
        self.assertEqual(len(name.name),10)
        self.assertEqual(name.email,'prs')

