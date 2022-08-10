from unicodedata import name
from django.contrib import admin
from django.urls import path,include
from . import views 

urlpatterns = [
 path('',views.index,name=''),
 path('Store_register/',views.Store_Register, name='Store_register'),
 path('Store_Details/',views.Store_Details,name='Store_Details'),
 path('Store_Manage/<int:pk>/',views.Store_Manage, name='Store_Manage'),
 path('Edit_Book/<int:pk>/',views.Edit_Book, name='Edit_Book'),
 path('Remove_book/<int:pk>/',views.Remove_book,name='Remove_book'),
 path('Add_Book',views.Add_Book,name='Add_Book'),
 path('Add_Book_To_store/<int:pk>/',views.Add_Book_To_store,name='Add_Book_To_store'),
 
 
]
