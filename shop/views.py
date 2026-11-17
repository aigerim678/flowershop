from django.shortcuts import render, get_object_or_404
from django.db.models import Prefetch

from .models import Category, Collection, Product
from cart.forms import CartAddProductForm


def product_list(request,
                 category_slug=None,
                 collection_slug=None):
    category = None
    collection = None
    all_collections = Collection.objects.all()
    products = Product.objects.filter(available=True) \
                              .select_related('category', 'collection')
    collections = None
    uncollected = None
    if category_slug:
        category = get_object_or_404(Category,
                                     slug=category_slug)
        products = products.filter(category=category)
    else:
        # Bouquets are grouped by collection: all of them on the home page,
        # or just one when filtering by collection
        collections = all_collections.prefetch_related(
            Prefetch('products', queryset=products.order_by('id'))
        )
        if collection_slug:
            collection = get_object_or_404(Collection,
                                           slug=collection_slug)
            collections = collections.filter(pk=collection.pk)
        else:
            uncollected = products.filter(collection__isnull=True)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'collection': collection,
                   'all_collections': all_collections,
                   'collections': collections,
                   'uncollected': uncollected,
                   'products': products})
    

def product_detail(request, id, slug):
    product = get_object_or_404(Product.objects.select_related('category', 'collection'),
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})
        