from unittest import mock

from django.test import TestCase
from django.urls import reverse

from shop.models import Product
from .models import Order


class OrderCreateTests(TestCase):
    fixtures = ['demo_catalog']

    @mock.patch('orders.views.order_created.delay')
    def test_checkout_creates_order_and_queues_email(self, delay):
        product = Product.objects.get(slug='love-letters')
        self.client.post(reverse('cart:cart_add', args=[product.id]),
                         {'quantity': 2, 'override': False})
        response = self.client.post(reverse('orders:order_create'), {
            'first_name': 'Aida', 'last_name': 'K', 'email': 'a@example.com',
            'address': 'Abay 1', 'postal_code': '050000', 'city': 'Almaty',
        })

        order = Order.objects.get()
        self.assertRedirects(response, reverse('payment:process'),
                             fetch_redirect_response=False)
        self.assertEqual(order.get_total_cost(), product.price * 2)
        delay.assert_called_once_with(order.id)
