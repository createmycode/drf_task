from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from .models import Product
from .serializers import ProductListSerializer, ProductDetailSerializer
from django.core.cache import cache

# Create your views here.
class ProductListCreate(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        # 게시글 목록 조회
        products = Product.objects.all()
        serializer = ProductListSerializer(products, many=True)  # 목록용 Serializer 사용
        return Response(serializer.data)
    
    def post(self, request):
        # 게시글 생성
        serializer = ProductDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ProductDetail(APIView):
    def get_object(self, product_id):
        return get_object_or_404(Product, id=product_id)
    
    def get(self, request, product_id):
        # 게시글 상세 조회
        product = self.get_object(product_id)
        product.view_count += 1
        product.save()

        serializer = ProductDetailSerializer(product) # 상세 Serializer 사용
        return Response(serializer.data)

    def put(self, request, product_id):
        # 게시글 수정
        product = self.get_object(product_id)
        serializer = ProductDetailSerializer(product, data=request.data, partial=True)

        if serializer.is_valid(raise_exception=True):
            if product.author == request.user:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        
            else: 
                return Response({
                'message':'수정권한이 없습니다.'
            }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, product_id):
        product = self.get_object(product_id)

        if request.user == product.author:
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        else:
            return Response({
                'message':'수정권한이 없습니다.'
            }, status=status.HTTP_400_BAD_REQUEST)