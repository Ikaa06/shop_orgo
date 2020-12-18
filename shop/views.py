from django.shortcuts import render, redirect
from django.views.generic import ListView

from shop.models import Products


class index(ListView):
    """ Основаная страница """

    def get(self, request, **kwargs):

        products = Products.objects.all()
        return render(request, "shop/index.html", {'products': products})


class details(ListView):
    """ Основаная страница """

    def get(self, request, slug):
        product = Products.objects.get(slug=slug)
        return render(request, "shop/details.html", {'product': product})
