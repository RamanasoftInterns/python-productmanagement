from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'created_at', 'is_published')
    list_display_links = ('id', 'name')
    list_filter = ('name', 'created_at')
    list_editable = ('is_published',)
    search_fields = ('name', 'price')
    ordering = ('price',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
