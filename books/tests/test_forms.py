
from django.test import TestCase
from books.forms import UserCreationForm

class TestForms(TestCase):

    def test_myform_test(self):
        form_data = {
            'username': 'userA', 'email': '1@gmail.com','password' : '123456789'
        }
        form = UserCreationForm(form_data)
        self.assertTrue(form.is_valid())