from django.shortcuts import render
from products.models import Product

# Create your views here.
def result_search(request):
    result = None
    try:
        produit = request.GET['search']
        result = Product.objects.filter(product_name_fr__icontains=produit)
    except:
        pass

    return render(request, 'pur_beurre/home.html', {'list_produit': result})
