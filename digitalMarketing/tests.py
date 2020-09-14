from django.test import TestCase
from django.shortcuts import get_object_or_404

# Create your tests here.

# Strong entities test (View function)

class DMServicesTestCase(TestCase):

    def test_can_get_DMService_form(self):
        response = self.client.get('/DMServices/create')
        self.assertEqual(response.status_code, 200)
