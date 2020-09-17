from django.test import TestCase
from django.shortcuts import get_object_or_404

# Create your tests here.

# Strong entities test (View function)

class DMServicesTestCase(TestCase):

    def test_can_get_DMService_form(self):
        response = self.client.get('/dmservice/create')
        self.assertEqual(response.status_code, 200)

class DMServicesDeleteTestCase(TestCase):

    def test_can_get_DMService_delete(self):
        response = self.client.get('/dmservice/delete')
        self.assertEqual(response.status_code, 200)

class DAServicesTestCase(TestCase):

    def test_can_get_DAService_form(self):
        response = self.client.get('/daservice/create')
        self.assertEqual(response.status_code, 200)

class ShowAllPageTestCase(TestCase):

    def test_can_get_all_services_page(self):
        response = self.client.get('/services/all')
        self.assertEqual(response.status_code, 200)


