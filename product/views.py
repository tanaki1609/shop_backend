from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from product.models import Product
from product.serializers import ProductSerializer


@api_view(['GET'])
def product_list_api_view(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def product_detail_api_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(data={'message': 'product not found'},
                        status=status.HTTP_404_NOT_FOUND)
    serializer = ProductSerializer(product, many=False)
    return Response(data=serializer.data)


@api_view(['GET'])
def test_api_view(request):
    dict_ = {
        'text': 'Hello world!',
        'int': 100,
        'float': 9.99,
        'bool': True,
        'list': [1, 2, 3],
        'dict': {'key': 'value'}
    }
    return Response(data=dict_)
