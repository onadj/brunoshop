from django.shortcuts import render
from .models import Product

# Create your views here.


def all_products(request):
    return render(request, 'products/products.html', context)


products = Product.objects.all()

context = {
    'products': products,
}
