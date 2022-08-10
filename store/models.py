from email.policy import default
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Books(models.Model):
    book_name = models.CharField(max_length=100, null=True)
    quantity = models.PositiveIntegerField(null=True)
    author_name = models.CharField(max_length=100, null=True)
    book_image = models.ImageField(default='default.jpg',upload_to='Book_Images')

    def __str__(self):
        return f'{self.book_name}'
        
class Store(models.Model):
    store_name = models.CharField(max_length=100, null=True)
    owner_name = models.CharField(max_length=100, null=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    book_name = models.ManyToManyField(Books)
    store_image = models.ImageField(default='default.jpg',upload_to='Store_Images')

    def __str__(self):
        return f'{self.store_name, self.customer}'