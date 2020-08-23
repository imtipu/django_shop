from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import *
from .models import *
# Create your views here.


def shop_home(request):
    return HttpResponse('ok')


class ProductList(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'products/list.html'

    # def get_context_data(self, *, object_list=None, **kwargs):

    def get_queryset(self):
        return Product.objects.all().prefetch_related('product_tags', 'product_variants', 'productimage_set')


# def products(request):
#     product_list = Product.objects.all().prefetch_related('product_tags', 'product_variants', 'productimage_set')
#     data = {
#         'title': 'Products',
#         'products': product_list,
#     }
#     return render(request, 'products/list.html', data)
