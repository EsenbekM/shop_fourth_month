from django.http import HttpRequest
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import ProductSerializer, ProductCreateValidateSerializer, CategorySerializer
from .models import Product, Category



@api_view(['GET'])
def index(request):
    data = {
        'intiger': 100,
        'float': 1.33,
        'bool': True,
        'list': [1,2,3,4],
        'text': "hello"
    }
    return Response(data)

class CategoryListAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]
    pagination_class = PageNumberPagination

class CategoryDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'

# @api_view(['GET', 'POST'])
# # @permission_classes([IsAuthenticated])
# def product_list_view(request: HttpRequest):
#     print(request.user)
#     if request.method == 'GET':
#         if request.user and request.user.is_authenticated:
#             products = Product.objects.all()
#             serializer = ProductSerializer(products, many=True)
#             return Response(data=serializer.data)
#         return Response(data={"message": "User dosn't exist!"})
#     elif request.method == 'POST':
#         serializer = ProductCreateValidateSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(status=status.HTTP_406_NOT_ACCEPTABLE, data={'message': 'error', 'errors': serializer.errors})
#         title = request.data['title']
#         price = request.data.get('price')
#         category = request.data.get('category')
#         text = request.data.get('text')



#         product = Product.objects.create(
#             title=title,
#             price=price,
#             category_id=category,
#             text=text
#         )

#         product.save()
#         return Response("Product succesfully crated!")


# @api_view(['GET', 'DELETE', 'PUT'])
# def product_detail_view(request: HttpRequest, id):
#     try:
#         product = Product.objects.get(id=id)
#     except Product.DoesNotExist:
#         return Response(
#             status=status.HTTP_404_NOT_FOUND,
#             data={
#                 "ERROR": "Product does not exist!"
#             }
#             )
#     if request.method == 'GET':
#         serializer = ProductSerializer(product, many=False)
#         return Response(data=serializer.data)
#     elif request.method == 'PUT':
#         product.title = request.data['title']
#         product.price = request.data['price']
#         product.category_id = request.data['category']
#         product.text = request.data['text']
#         product.save()
#         return Response(data={'message': 'Product updated'})
#     elif request.method == 'DELETE':
#         product.delete()
#         return Response(data={'message': 'Product deleted'})
    
