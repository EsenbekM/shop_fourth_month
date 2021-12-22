from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Product, Category, Tag, Review

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id', 
            'title', 
            'price', 
            'created', 
            'updated', 
            'category'
            ]


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'


class TagsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'



class ProductCreateValidateSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=1, max_length=200)
    description = serializers.FloatField() 
    text = serializers.CharField()
    category = serializers.IntegerField()

    def validate_category(self, category):
        try:
            Category.objects.get(id=category)
        except Category.DoesNotExist:
            raise ValidationError("This category doesn't exist!")

    def validate_title(self, title):
        if Product.objects.filter(title=title):
            raise ValidationError("This title already exist!")  