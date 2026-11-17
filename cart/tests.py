from decimal import Decimal

from django.test import TestCase
from django.urls import reverse

from shop.models import Product


class CartTests(TestCase):
    fixtures = ['demo_catalog']

    def test_add_and_remove(self):
        product = Product.objects.get(slug='love-letters')
        self.client.post(reverse('cart:cart_add', args=[product.id]),
                         {'quantity': 3, 'override': False})
        response = self.client.get(reverse('cart:cart_detail'))
        self.assertEqual(response.context['cart'].get_total_price(),
                         product.price * 3)

        self.client.post(reverse('cart:cart_remove', args=[product.id]))
        response = self.client.get(reverse('cart:cart_detail'))
        self.assertEqual(response.context['cart'].get_total_price(), Decimal(0))
