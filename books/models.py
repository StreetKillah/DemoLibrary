from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

class Book(models.Model):
    name=models.CharField(verbose_name='Name', db_index=True, unique=True,max_length=15)
    author=models.CharField(verbose_name='Author', db_index=True, max_length=20)
    user=models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
