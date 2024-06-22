
from django.test import TestCase
from django.urls import reverse, resolve

from books.models import User


#ログインしていない
class TestsStatusCord(TestCase):

    def test_book_status_code(self):
        response = self.client.get('/book/eX_eEAAAQBAJ/')
        self.assertRedirects(response, '/login/?next=/book/eX_eEAAAQBAJ/')

    def test_mylibrary_status_code(self):
        response = self.client.get('/mylibrary/')
        self.assertRedirects(response, '/login/?next=/mylibrary/')

    def test_profile_status_code(self):
        response = self.client.get('/profile/')
        self.assertRedirects(response, '/login/?next=/profile/')
        

# ログインしている場合
class TestsLoginStatusCord(TestCase):
    
    def setUp(self):
        user = User.objects.create(username='userA', password='qwerty', email='1aaaaa2@2aaaaa1.com')
        self.client.force_login(user)
        
    def test_book_login_status_code(self):
        response = self.client.get('/book/eX_eEAAAQBAJ/')
        self.assertEqual(response.status_code, 200)

    def test_mylibrary_status_code(self):
        response = self.client.get('/mylibrary/')
        self.assertEqual(response.status_code, 200)

    def test_profile_status_code(self):
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)