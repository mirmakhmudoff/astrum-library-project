from django.contrib import admin
from .models import User, Book, BorrowRecord

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_admin', 'is_staff')
    list_filter = ('is_admin', 'is_staff', 'is_active')
    search_fields = ('username', 'email')
    ordering = ('id',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'genre', 'is_available')
    list_filter = ('genre', 'is_available')
    search_fields = ('title', 'author')
    ordering = ('id',)

@admin.register(BorrowRecord)
class BorrowRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'book', 'borrow_date', 'return_date')
    list_filter = ('borrow_date', 'return_date')
    search_fields = ('user__username', 'book__title')
    ordering = ('borrow_date',)
