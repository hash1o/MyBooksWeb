

import requests

from django.views.generic import ListView, TemplateView,View,UpdateView,CreateView,DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect,render
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.urls import reverse


from books.forms import UserCreationForm
from books.models import MemoBook,Profile

class BookSearchView(TemplateView):
    template_name = 'pages/index.html'
    
    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q')
        books = []

        if not query:
            return context

        url = f'https://www.googleapis.com/books/v1/volumes?q={query}'
        response = requests.get(url)
        if not response.status_code == 200:
            return context

        data = response.json()
        books = data.get('items', [])

        context['books'] = books

        return context

class BookDetailView(LoginRequiredMixin,DetailView):
    template_name = 'pages/book.html'
    model = MemoBook

    def get_queryset(self):
        return MemoBook.objects.filter(user=self.request.user)

    def get(self, request, book_id):
        query = request.GET.get('q')
        if query:
            redirect_url = reverse('index') + f'?q={query}'
            return redirect(redirect_url)

        response = requests.get(f'https://www.googleapis.com/books/v1/volumes/{book_id}')
        book = response.json()

        #見つからなかった場合にエラーとなる(例外処理しない方法でやります)
        #memo = MemoBook.objects.get(book_id=book_id) 

        queryset = self.get_queryset()
        
        if not queryset:
            context = { "book":book ,"memo":{"memo":""}}
            return render(request, self.template_name, context)

        for model in queryset:
                
            if not model.book_id == book_id:
                continue
                
            context = { "book":book ,"memo":model }
            return render(request, self.template_name, context)
        

        context = { "book":book ,"memo":{"memo":""}}
        return render(request, self.template_name, context)

    def post(self, request, book_id):
        memoText = request.POST.get('memoText')

        response = requests.get(f'https://www.googleapis.com/books/v1/volumes/{book_id}')
        book_data = response.json()
        
        title = book_data.get('volumeInfo', {}).get('title', 'タイトル無し')

        #MemoBook.objects.update_or_create(user=request.user,defaults={"memo":memoText,"title":title,"book_id":book_id})
        MemoBook.objects.update_or_create(
            book_id=book_id,
            user=request.user,
            defaults={
                "memo": memoText,
                "title": title,
                "bookjson":book_data,
            }
        )
        
        
        return redirect("book",book_id=book_id)
    
class BookLibraryView(LoginRequiredMixin,ListView):
    template_name = 'pages/mylibrary.html'

    def get_queryset(self):
        return MemoBook.objects.filter(user=self.request.user)

    def get_context_data(self,**kwargs) -> dict:
    
        context = super().get_context_data(**kwargs)

        mybooks = []
        queryset = self.get_queryset()

        for model in queryset:
            
            query = model.book_id
            if not query:
                continue

            data = model.bookjson

            mybooks.append(data)

        context['books'] = mybooks
        return context
    
    def get(self, request, *args, **kwargs):

        query = request.GET.get('q')
        if query:
            redirect_url = reverse('index') + f'?q={query}'
            print(redirect_url)
            return redirect(redirect_url)

        #親クラスのget()を実行する
        return super().get(request, *args, **kwargs)