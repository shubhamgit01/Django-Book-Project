from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from .forms import BookForm,UserForm
from .models import Book
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required

# Create your views here.
def index_view(request):
    return render(request,'app/index.html')
@login_required
def books_view(request):
    u_id=request.session.get('_auth_user_id')
    all_books=Book.objects.filter(user_id=u_id)
    return render(request,'app/books.html',{'books':all_books})
@login_required
def new_book_view(request):
    if request.method =="POST":
        bf=BookForm(request.POST,request.FILES)
        if bf.is_valid():
            book=bf.save(commit=False)
            u_id=request.session.get('_auth_user_id')
            book.user_id=u_id
            book.save()
        return redirect('/app/books/')
    bf=BookForm()
    return render(request,'app/new_book.html',{'form':bf})
@login_required
def edit_view(request):
    if request.method=='POST':
        book_id=request.POST.get('book_id')
        book=Book.objects.get(id=book_id)
        bf=BookForm(request.POST,request.FILES,instance=book)
        bf.save()
        bf=BookForm(initial=model_to_dict(book))
            
    book_id=request.GET.get('book_id')
    book=Book.objects.get(id=book_id)
    bf=BookForm(initial=model_to_dict(book))
    return render(request,'app/edit_book.html',{'form':bf,'book_id':book_id})
@login_required
def del_view(request):
    book_id=request.GET.get('book_id')
    book=Book.objects.get(id=book_id)
    book.delete()
    return redirect('/app/books/')

def signup_view(request):
    if request.method == "POST":
        uf=UserForm(request.POST)
        if uf.is_valid:
            user=uf.save(commit=False)
            user.set_password(user.password)
            user.save()
            return redirect('/accounts/login')


    uf=UserForm()
    return render(request,'app/signup.html',{'form':uf})



