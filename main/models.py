from django.contrib.auth.models import User
from django.db import models

class BookUser(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    address=models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

class Customer (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.PositiveBigIntegerField(unique=True, null=True)
    profile_img = models.ImageField(upload_to='customer_imgs/', null=True)

    def __str__(self):
        return self.user.username


class Book(models.Model):
    
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True,related_name='customer_books')
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(
        upload_to='product_imgs/', null=True, blank=True)
    author = models.CharField(max_length=100)
    slug = models.CharField(max_length=200, unique=True, null=True)
    published_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return self.title





class Review(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True,related_name='reviews_user')
    book = models.ForeignKey(Book,on_delete=models.CASCADE, null=True,related_name='book_ratings')
    rating = models.IntegerField()
    comment = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.rating} - {self.comment}'
