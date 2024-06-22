from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import books,account


urlpatterns = [
    path('', books.BookSearchView.as_view(),name="index"),
    path('book/<str:book_id>/', books.BookDetailView.as_view(),name="book"),
    path('mylibrary/', books.BookLibraryView.as_view(),name="mylibrary"),
    path('profile/', account.ProfileUpdateView.as_view(),name="profile"),
    #path('account/', account.AccountUpdateView.as_view(),name="account"),
    path('login/', account.Login.as_view(),name="login"),
    path('logout/', LogoutView.as_view(),name="logout"),
    path('signup/', account.SignUpView.as_view(),name="signup"),
    
]