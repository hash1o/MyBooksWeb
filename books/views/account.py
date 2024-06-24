
from django.views.generic import UpdateView,CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model


from books.forms import UserCreationForm
from books.models import MemoBook,Profile

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = '/login/'
    template_name = 'pages/login_signup.html'
 
    def form_valid(self, form):
        return super().form_valid(form)
 
 
class Login(LoginView):
    template_name = 'pages/login_signup.html'
 
    def form_valid(self, form):
        return super().form_valid(form)
 
    def form_invalid(self, form):
        return super().form_invalid(form)
 
 
class AccountUpdateView(UpdateView):
    model = get_user_model()
    template_name = 'pages/account.html'
    fields = ('username', 'email',)
    success_url = '/account/'
 
    def get_object(self):
        # URL変数ではなく、現在のユーザーから直接pkを取得
        self.kwargs['pk'] = self.request.user.pk
        return super().get_object()
 
 
class ProfileUpdateView(LoginRequiredMixin,UpdateView):
    model = Profile
    template_name = 'pages/profile.html'
    fields = ('name', 'zipcode', 'prefecture',
              'city', 'address1', 'address2', 'tel','profile_image')
    success_url = '/profile/'
 
    def get_object(self):
        # URL変数ではなく、現在のユーザーから直接pkを取得
        self.kwargs['pk'] = self.request.user.pk
        return super().get_object()