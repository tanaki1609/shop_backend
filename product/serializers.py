from rest_framework import serializers
from .models import Product, Category, Tag, Review
from rest_framework.exceptions import ValidationError


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


class ProductCreateUpdateSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=1, max_length=100)
    text = serializers.CharField(required=False, default='No text')
    price = serializers.FloatField(min_value=1, max_value=1000000000)
    amount = serializers.IntegerField()
    is_active = serializers.BooleanField(default=True)
    category_id = serializers.IntegerField()
    tags = serializers.ListField(child=serializers.IntegerField())

    def validate_category_id(self, category_id):  # 10
        try:
            Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            raise ValidationError('Category does not exists!')
        return category_id

    def validate_tags(self, tags):  # [1,2,10]
        tags_from_db = Tag.objects.filter(id__in=tags)
        if len(tags_from_db) != len(tags):
            raise ValidationError('Tag does not exists!')
        return tags
