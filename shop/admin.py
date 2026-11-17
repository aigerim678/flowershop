from django.contrib import admin
from .models import Category, Collection, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['number', 'name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'collection', 'category', 'mood', 'price',
                    'available', 'created', 'updated']
    list_filter = ['collection', 'category', 'available', 'created']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}
    