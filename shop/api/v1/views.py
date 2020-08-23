from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.generics import *
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from .serializers import *


class ProductList(ListAPIView):
    permission_classes = [AllowAny, ]
    authentication_classes = []
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get_queryset(self):
        return Product.objects.prefetch_related('product_tags', 'product_variants', 'product_images').all()


@api_view(('GET',))
@permission_classes([AllowAny, ])
@authentication_classes([])
def home_categories(request):
    queryset = ProductCategory.objects.all().order_by('title')
    serializer = ProductCategorySerializer(queryset, many=True)
    data = serializer.data

    return Response(data, status=status.HTTP_200_OK)


@api_view(('GET',))
@permission_classes([AllowAny, ])
@authentication_classes([])
def homepage_banner_sliders(request):
    queryset = HomePageBannerSlider.objects.all()
    serializer = HomePageBannerSliderSerializer(queryset, context={"request": request}, many=True)
    data = serializer.data

    return Response(data, status=status.HTTP_200_OK)


class ProductDetailAPIView(RetrieveAPIView):
    permission_classes = [AllowAny, ]
    authentication_classes = []
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_url_kwarg = 'slug'
    lookup_field = 'slug'


class ProductCategoryDetailView(RetrieveAPIView):
    permission_classes = [AllowAny, ]
    authentication_classes = []
    serializer_class = ProductCategorySerializer
    queryset = ProductCategory.objects.all()
    lookup_url_kwarg = 'slug'
    lookup_field = 'slug'


class ProductCategoryProductList(ListAPIView):
    permission_classes = [AllowAny, ]
    authentication_classes = []
    serializer_class = ProductSerializer
    queryset = None

    def get_queryset(self):
        return Product.objects.prefetch_related(
            'product_tags', 'product_variants', 'product_images').filter(
            category__slug=self.kwargs['slug']
        ).order_by('title')


@api_view(('GET',))
@permission_classes([AllowAny, ])
@authentication_classes([])
def cart_items_list(request):
    product_ids = request.GET.get('ids').split(',')
    print(product_ids)
    products = Product.objects.prefetch_related('product_tags', 'product_variants', 'product_images').filter(id__in=product_ids).order_by('id')
    serializer = ProductSerializer(products, many=True, context={'request': request})
    return Response(serializer.data, status=status.HTTP_200_OK)
