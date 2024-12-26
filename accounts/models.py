from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('이메일은 필수입니다')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    email = models.EmailField('이메일', unique=True)
    username = models.CharField('닉네임', max_length=150, unique=True) 
    profile_image = models.ImageField('프로필 이미지', upload_to='profile_images/', blank=True, null=True)
    first_name = models.CharField("first_name", max_length=50)
    last_name = models.CharField("last_name", max_length=50)
    nickname = models.CharField('닉네임', max_length=50)
    birth = models.DateField(verbose_name='생일')
    gender = models.CharField(verbose_name='성별', max_length=5, null=True, blank=True)
    introduce = models.CharField('자기소개', max_length=150, null=True, blank=True)
    
    USERNAME_FIELD = 'email'    # 로그인 시 이메일 사용
    REQUIRED_FIELDS = []        # email은 자동으로 필수

    objects = CustomUserManager()

    def __str__(self):
        return self.email
