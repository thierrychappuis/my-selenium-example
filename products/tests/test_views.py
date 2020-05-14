from django.test import TestCase
from django.urls import reverse

from products.views import product_sheet, result_search


class ProductTestViews(TestCase):

    def views_result_search(self):
        url = result_search()
        response = self.client.get(reverse('products/'+"?q=pizza"))
        self.assertEqual(response.status_code, 200)

    def views_product_sheet(self):
        response = self.client.get('products/details/')
        self.assertEqual(response.status_code, 200)

    def views_favorites(self):
        pass
