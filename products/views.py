from django.shortcuts import render
from products.models import Product

# Create your views here.
def result_search(request):
    result = None
    try:
        product_search = request.GET['q']
        result = Product.objects.filter(product_name_fr__icontains=product_search)
    except:
        pass

    return render(request, 'products/result_search.html', {'result_search': result})
