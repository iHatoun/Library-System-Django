from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Author, Category, Book, Member, Staff, Loan, Review, ActionLog

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Member)
admin.site.register(Staff)
admin.site.register(Loan)
admin.site.register(Review)
admin.site.register(ActionLog)
