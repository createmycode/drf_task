from django.db import models
from django.conf import settings

# Create your models here.
class Product(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='products')
    title = models.CharField('제목', max_length=100)
    content = models.TextField('내용')
    product_image = models.ImageField('상품 이미지', upload_to='product_images/')
    created_at = models.DateTimeField('작성일', auto_now_add=True)
    updated_at = models.DateTimeField('수정일', auto_now=True)
    view_count = models.PositiveBigIntegerField('조회수', default=0) # 조회수 필드 추가

    def __str__(self):
        return self.title
    