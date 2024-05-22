
from django.contrib import admin
from django.urls import path, include
from .import views
from rest_framework import routers

route = routers.DefaultRouter()
route.register('', views.BookViewSet)
route.register('reviews', views.ReviewViewSet)

urlpatterns = [
    path('all_book/', views.BookViewSet.as_view(), name='book_list'),    
    path('customer_book/<int:pk>', views.BookListViewSet.as_view(), name='book_list_view'),    
    path('book_detail/<int:pk>/', views.BookDetailsViewSet.as_view(), name='bbok_details'),    
    path('book-reviews/', views.ReviewViewSet.as_view(), name='review_list'),
    path('review_detail/<int:pk>/', views.ReviewDetailsViewSet.as_view(), name='review_list'),
    path('review_book/<int:pk>/', views.ReviewDetailViewSet.as_view(), name='review_details'),
    path('customer_login/', views.customer_login, name='login'),
    path('customer_register/', views.customer_register, name='register'),
    path('customer/<int:pk>/', views.CustomerDetail.as_view()),
    path('user/<int:pk>/', views.UserDetail.as_view()),
    path('customer-change-password/<int:pk>/', views.CustomerChangePassword),
    
]
