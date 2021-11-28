from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=None,null=True)
    title=models.CharField(max_length=45)
    author=models.CharField(max_length=40)
    cover=models.ImageField(upload_to='book_covers')
    price=models.PositiveIntegerField()

