from rest_framework import serializers
from .models import  Book, Review,BookUser, Customer
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name',
                  'last_name',  'email']  


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'user', 'phone', 'profile_img']

        def __init__(self, *args, **kwargs):
            super(CustomerSerializer, self).__init__(*args, **kwargs)
            self.Meta.depth = 1

class CustomerDetailSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
            response = super().to_representation(instance)
            response['user'] = UserSerializer(instance.user).data
            return response

    class Meta:
        model = Customer
        fields = ['id', 'user', 'phone', 'profile_img']

    def __init__(self, *args, **kwargs):
        super(CustomerDetailSerializer, self).__init__(*args, **kwargs)

class BookSerializer(serializers.ModelSerializer):
    book_ratings = serializers.StringRelatedField(
        many=True, read_only=True)
    class Meta:
        model = Book
        fields = ['id','customer','description','slug' ,'image','title', 'author', 'published_date', 'isbn','book_ratings']


        # def to_representation(self, instance):
        #     response = super().to_representation(instance)
        #     response['user'] = UserSerializer(instance.user).data
        #     return response

    # def __init__(self, *args, **kwargs):
    #         super(BookSerializer, self).__init__(*args, **kwargs)
            # self.Meta.depth = 1

class BookDetailSerializer(serializers.ModelSerializer):
    book_ratings = serializers.StringRelatedField(
        many=True, read_only=True)
    class Meta:
        many=True
        model = Book
        fields = ['id','customer','description' ,'image','slug','title', 'author', 'published_date', 'isbn','book_ratings']

    def __init__(self, *args, **kwargs):
            super(BookDetailSerializer, self).__init__(*args, **kwargs)
            self.Meta.depth = 1

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'customer','book', 'rating', 'comment', 'created_date']



class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'customer','book', 'rating', 'comment', 'created_date']

    
        def to_representation(self, instance):
            response = super().to_representation(instance)
            response['customer'] = CustomerSerializer(instance.customer).data
            response['book'] = BookSerializer(instance.book).data
            return response

    # def __init__(self, *args, **kwargs):
    #         super(ReviewSerializer, self).__init__(*args, **kwargs)
    #         self.Meta.depth = 1
