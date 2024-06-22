
from django.test import TestCase
from django.urls import reverse, resolve

from books.views import books,account


#ログインしていない
class TestsUrls(TestCase):

    def test_index_url(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func.view_class, books.BookSearchView)

    def test_login_url(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func.view_class, account.Login)
        
    def test_signup_url(self):
        url = reverse('signup')
        self.assertEqual(resolve(url).func.view_class, account.SignUpView)