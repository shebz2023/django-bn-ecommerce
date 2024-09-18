from django.shortcuts import render
from store.models import Product

def say_hello(request):
    queryset = Product.objects.all()[:5]
    return render(request, "hello.html", {"name": "Mosh", "products": list(queryset)})
