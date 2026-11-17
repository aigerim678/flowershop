from django.test import TestCase
from django.urls import reverse

from .models import Product


class CatalogTests(TestCase):
    fixtures = ['demo_catalog']

    def test_product_list(self):
        response = self.client.get(reverse('shop:product_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Love Letters')

    def test_category_filter(self):
        response = self.client.get(
            reverse('shop:product_list_by_category', args=['peonies'])
        )
        self.assertContains(response, 'Dark Desire')
        self.assertNotContains(response, 'Love Letters')

    def test_home_groups_bouquets_by_collection(self):
        response = self.client.get(reverse('shop:product_list'))
        collections = list(response.context['collections'])
        self.assertEqual([c.name for c in collections],
                         ['Velvet Reverie', 'Tender Ruins', 'First Love',
                          'Strange Eden', 'Wild Poetry'])
        self.assertEqual(len(collections[1].products.all()), 6)
        self.assertContains(response, 'Faded Poetry')

    def test_collection_filter(self):
        response = self.client.get(
            reverse('shop:product_list_by_collection', args=['first-love'])
        )
        self.assertEqual([c.name for c in response.context['collections']],
                         ['First Love'])
        self.assertContains(response, 'Butterflies')
        self.assertNotContains(response, 'Love Letters')

    def test_product_detail(self):
        product = Product.objects.get(slug='love-letters')
        response = self.client.get(product.get_absolute_url())
        self.assertEqual(response.status_code, 200)
