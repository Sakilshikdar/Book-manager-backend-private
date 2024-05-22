from rest_framework import viewsets, generics
from .models import Book, Review,BookUser, Customer
from .serializers import BookSerializer, ReviewSerializer, UserSerializer,ReviewDetailSerializer,BookDetailSerializer,CustomerDetailSerializer
from  django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password


@csrf_exempt
def customer_register(request):
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    username = request.POST.get('username')
    password = request.POST.get('password')
    mobile = request.POST.get('mobile')

    try:
        # Create a new user
        user = User.objects.create_user(
            username=username, email=email, password=password, first_name=first_name, last_name=last_name)
        if user:
            try:
                customer = Customer.objects.create(user=user, phone=mobile)
                msg = {
                    'bool': True,
                    'user': user.id,
                    'customer': customer.id,
                    'msg': 'You have successfully registered.You can now login.'
                }
            except:
                msg = {
                    'bool': False,
                    'msg': 'mobile already exists'
                }
        else:
            msg = {
                'bool': False,
                'msg': 'Oops! Something went wrong. Please try again later.'
            }
    except IntegrityError:
        msg = {
            'bool': False,
            'msg': 'username already exist'
        }
    return JsonResponse(msg)



@csrf_exempt
def customer_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user:
        customer = Customer.objects.get(user=user)
        msg = {
            'bool': True,
            'user': user.username,
            'id': customer.id,
        }
    else:
        msg = {
            'bool': False,
            'msg': 'Invalid username or password'
        }

    return JsonResponse(msg)



@csrf_exempt
def CustomerChangePassword(request, customer_id):
    password = request.POST.get('password')
    customer = Customer.objects.get(id=customer_id)
    user = customer.user
    user.password = make_password(password)
    user.save()
    msg = {
        'bool': True,
        'msg': 'Password changed successfully'
    }
    return JsonResponse(msg)

class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerDetailSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class BookUserViewSet(generics.ListCreateAPIView):
    queryset = BookUser.objects.all()
    serializer_class = UserSerializer
   

class BookViewSet(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookListViewSet(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        customer = self.kwargs['pk']
        qs = qs.filter(customer__id=customer)
        return qs
        
class BookListViewSet(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        customer = self.kwargs['pk']
        qs = qs.filter(customer__id=customer)
        return qs
   

class BookDetailsViewSet(generics.RetrieveUpdateDestroyAPIView):
    # queryset = Book.objects.all()
    serializer_class = BookDetailSerializer

    def get_queryset(self):
        book_id = self.kwargs['pk']
        return Book.objects.filter(id=book_id)



class ReviewDetailsViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
   

class ReviewViewSet(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    
   

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)
   

class ReviewDetailViewSet(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        book_id = self.kwargs['pk']
        qs = qs.filter(book__id=book_id)
        return qs

class UserProfileView(generics.RetrieveUpdateAPIView):
    queryset = BookUser.objects.all()
    serializer_class = UserSerializer
   

    def get_object(self):
        return self.request.user
