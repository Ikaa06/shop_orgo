from django.shortcuts import render, redirect
from django.views.generic import ListView


class index(ListView):
    """ Основаная страница """

    def get(self, request, **kwargs):
        return render(request, "shop/index.html")


class details(ListView):
    """ Основаная страница """

    def get(self, request, **kwargs):
        return render(request, "shop/details.html")
