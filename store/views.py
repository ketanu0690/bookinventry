from http.client import HTTPResponse
from tkinter.tix import Select
from django.shortcuts import render, redirect
from django.http import HttpResponse
import json
import requests
from django.contrib.auth.decorators import login_required
from .forms import BooksForm, StoreForm
from .models import Books,Store
from django.contrib.auth.models import User


@login_required(login_url='user_login')
def index(request):
    URL = "https://www.googleapis.com/books/v1/volumes?q=books:keyes&startIndex=0&maxResults=7&key=AIzaSyC9dqkMwlQv6rzXos3NFLWLcizJTZR5BGE"
    r = requests.get(url=URL)
    data = r.json()
    books = data['items']
    return render(request, 'dashboard/index.html', {"data": books})



# Store CRUD 
@login_required(login_url='user_login')
def Store_Register(request):
    store = Store.objects.all()
    if request.method == 'POST':
            form = StoreForm(request.POST)
            if form.is_valid():
                form.instance.customer = User.objects.get(id = request.user.id)
                form.save()
                return redirect('Store_Details')
    else:
        form = StoreForm()
    context={
        'form':form
    }    

    return render(request, 'dashboard/store_register.html',context)

@login_required(login_url='user_login')
def Store_Details(request): 
    user_id = request.user.id
    store = Store.objects.filter(customer=user_id)
    return render(request, 'dashboard/store_details.html',{'store':store})


@login_required(login_url='user_login')    
def Store_Manage(request,pk):

    store = Store.objects.filter(id=pk) 
    Filterbook = []
    for i in store:
        Filterbook.append(i.book_name.all())
    SelectBooks=[]
    for j in range(0,len(Filterbook[0])):  
        SelectBooks.append(Books.objects.filter(book_name=Filterbook[0][j]))

    context={
        'books':SelectBooks,
        'store_id':pk
    }       


    return render(request, 'dashboard/store_inventory.html',context)

# book CRUD
@login_required(login_url='user_login')
def Add_Book_To_store(request,pk):
    book = Store.objects.get(id=pk)
    if request.method == 'POST':
        form = StoreForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('Store_Details')
    else:
        form = StoreForm(instance=book)
    context = {
        'form': form,
    }

    return render(request,'dashboard/Add_book_to_store.html',context)

@login_required(login_url='user_login')
def Add_Book(request):
    if request.method == 'POST':
                form = BooksForm(request.POST)
                if form.is_valid():
                    form.save()
                    form = BooksForm()
                    return redirect("")
    else:
        form = BooksForm()
        book = Books.objects.all()


    context={
        'form':form,
        'books':book
    }    

    return render(request, 'dashboard/Add_book.html',context)

@login_required(login_url='user_login')
def Edit_Book(request,pk):
    book = Books.objects.get(id=pk)
    if request.method == 'POST':
        form = BooksForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('Store_Details')
    else:
        form = BooksForm(instance=book)
    context = {
        'form': form,
    }



    return render(request, 'dashboard/book_edit.html',context)

@login_required(login_url='user_login')
def Remove_book(request,pk):

    item = Books.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('Store_Details')
    context = {
        'item': item
    }
    return render(request, 'dashboard/book_delete.html', context)
