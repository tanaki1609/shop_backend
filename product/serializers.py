from rest_framework import serializers
from .models import Product, Category, Tag, Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text stars'.split()


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'id name'.split()


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = 'id name'.split()


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    tags = TagSerializer(many=True)
    category_str = serializers.SerializerMethodField()
    product_reviews = ReviewSerializer(many=True)
    filtered_reviews = ReviewSerializer(many=True)

    class Meta:
        model = Product
        fields = 'id title price category tags category_str' \
                 ' tag_list product_reviews filtered_reviews'.split()

    def get_category_str(self, product):
        try:
            return product.category.name
        except:
            return 'no category!'
