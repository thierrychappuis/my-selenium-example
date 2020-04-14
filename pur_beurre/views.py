from django.shortcuts import render
from django.urls import reverse

from products.models import Category


def home(request):
    category = Category.objects.all()
    return render(request, 'pur_beurre/home.html', {'list_category': category})
