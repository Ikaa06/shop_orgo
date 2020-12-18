from django.contrib import admin

from shop.models import BasicInfo, Products, ProductImage, Reviews, Reservation


@admin.register(BasicInfo)
class BasicInfo_admin(admin.ModelAdmin):
    list_display = ('id',)


class ReviewInline(admin.TabularInline):
    """Отзывы на странице товара"""
    model = Reviews
    extra = 1


class ProductImageInline(admin.StackedInline):
    model = ProductImage
    max_num = 10
    extra = 0


@admin.register(Products)
class Products_admin(admin.ModelAdmin):
    list_display = ('name', 'title', 'price', 'available', 'created', 'updated')
    inlines = [ProductImageInline, ReviewInline]
    list_editable = ('price', 'available')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Reservation)
class Reservation_admin(admin.ModelAdmin):
    list_display = ('name', 'email', 'product', 'available', 'created', 'updated')
    list_editable = ('available',)
