from django.test import TestCase
from django.shortcuts import get_object_or_404

# Create your tests here.

class TestViews(TestCase):
    
    def test_get_home_page(self):
        response=self.client.get('/')
        self.assertEqual(response.status_code, 200)