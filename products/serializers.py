from rest_framework import serializers
from .models import Product

class ProductListSerializer(serializers.ModelSerializer):
    # 게시글 목록 조회 Serializer
    author = serializers.ReadOnlyField(source='author.username') # author필드에 작성자의 유저네임만 출력

    class Meta:
        model = Product
        fields = ('id','author','title','created_at','view_count')


class ProductDetailSerializer(serializers.ModelSerializer):
    # 게시글 상세 조회 및 생성
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Product
        fields = ('id','author','title','content','product_image','created_at','updated_at','view_count')


class ProductImageSerializer(serializers.ModelSerializer):
    product_image = serializers.SerializerMethodField()


    

