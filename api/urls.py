from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookListCreate.as_view()),
    path('books/<int:pk>/', views.BookDetail.as_view()),
    path('authors/', views.AuthorListCreate.as_view()),
    path('categories/', views.CategoryListCreate.as_view()),
    path('members/', views.MemberListCreate.as_view()),
    path('loans/', views.LoanListCreate.as_view()),
    path('reviews/', views.ReviewListCreate.as_view()),
]
