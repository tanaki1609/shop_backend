from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from product.models import Product, Category
from product.serializers import ProductSerializer, ProductCreateUpdateSerializer


@api_view(['GET', 'POST'])
def product_list_api_view(request):
    if request.method == 'GET':
        """LIST"""
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        """CREATE"""
        serializer = ProductCreateUpdateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data=serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        title = serializer.validated_data.get('title')
        text = serializer.validated_data.get('text')
        price = serializer.validated_data.get('price')
        amount = serializer.validated_data.get('amount')
        is_active = serializer.validated_data.get('is_active')
        category_id = serializer.validated_data.get('category_id')
        tags = serializer.validated_data.get('tags')
        product = Product.objects.create(title=title, text=text, price=price,
                                         amount=amount, is_active=is_active,
                                         category_id=category_id)
        product.tags.set(tags)
        product.save()
        return Response(data=ProductSerializer(product).data,
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail_api_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(data={'message': 'product not found'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ProductSerializer(product, many=False)
        return Response(data=serializer.data)
    elif request.method == 'PUT':
        serializer = ProductCreateUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        product.title = request.data.get('title')
        product.text = request.data.get('text')
        product.price = request.data.get('price')
        product.amount = request.data.get('amount')
        product.is_active = request.data.get('is_active')
        product.category_id = request.data.get('category_id')
        product.tags.set(request.data.get('tags'))
        product.save()
        return Response(data=ProductSerializer(product).data)
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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
