from django.test import TestCase

# Create your tests here.


class TestViews(TestCase):

    def test_get_all_customer_page(self):
        response = self.client.get('/all-customer/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'customer/all-customer.template.html')
