from django.contrib import admin

from .models import Product, CartItem, ProductImage, Category, Review, Order, OrderItem


admin.site.register(CartItem)
admin.site.register(ProductImage)
admin.site.register(Order)
admin.site.register(OrderItem)

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price']
    inlines = [ProductImageInline]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'created_at']
