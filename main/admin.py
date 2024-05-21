from django.contrib import admin
from .models import Book, Review,BookUser, Customer
# from django.contrib.auth.models import User
# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = ['title','author' ]
    prepopulated_fields = {'slug': ('title',)}
    
class customerAdmin(admin.ModelAdmin):
    list_display = ['get_username', 'phone']

    def get_username(self, obj):
        return obj.user.username
admin.site.register(Book, BookAdmin)
admin.site.register(Review)
admin.site.register(BookUser)
admin.site.register(Customer, customerAdmin)
# admin.site.register(User)

