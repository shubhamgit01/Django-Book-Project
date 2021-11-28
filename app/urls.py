from django.urls import path
from . import views
urlpatterns=[
    path('index/',views.index_view),
    path('books/',views.books_view),
    path('new/',views.new_book_view),
    path('edit/',views.edit_view),
    path('del/',views.del_view),
    path('signup/',views.signup_view)
]