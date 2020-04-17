from django.shortcuts import render
from products.models import Product

# Create your views here.
def result_search(request):
    result = None
    try:
        product_search = request.GET['q']
        product = Product.objects.filter(product_name_fr__icontains=product_search).first()
        substituts = product.better_products()

    except KeyError:
        print('Pas de requête')

    return render(request, 'products/result_search.html', {'substituts': substituts})
