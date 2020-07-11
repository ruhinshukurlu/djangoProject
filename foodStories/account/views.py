from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import DetailView, UpdateView
from django.urls import reverse_lazy
from django.views import View
from account.forms import RegisterForm,LoginForm,ChangePasswordForm,ResetPasswordForm,SetPasswordForm, UserEditForm
from django.contrib.auth.views import LoginView,PasswordChangeView,PasswordChangeDoneView,PasswordResetView, PasswordResetConfirmView
# Create your views here.

from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterView(CreateView):
    template_name = 'accounts/register.html'
    model = User
    form_class = RegisterForm
    success_url = reverse_lazy('stories:Home')

class LoginView(LoginView):
    template_name = 'accounts/login.html'
    form_class = LoginForm

    def get_success_url(self, **kwargs): 
        return reverse_lazy('stories:Home')

class ChangePasswordView(PasswordChangeView):
    template_name = 'accounts/change_password.html'
    form_class = ChangePasswordForm
    success_url = reverse_lazy('stories:Home')

class ChangePasswordDoneView(PasswordChangeDoneView):
    template_name = 'change_password_done.html'
    

class ResetPasswordView(PasswordResetView):
    template_name = 'forget_password.html'
    form_class = ResetPasswordForm
    email_template_name = 'reset_password.html'
    success_url = reverse_lazy('stories : Home')

class ResetPasswordConfirmView(PasswordResetConfirmView):
    template_name = 'reset_password.html'
    form_class = SetPasswordForm
    success_url = reverse_lazy('account : login')
    
class UserProfileView(DetailView):
    model = User
    template_name = 'user-profile.html'
    context_object_name = 'user'
    
class UpdateUserView(UpdateView):
    model = User
    form_class = UserEditForm
    template_name = 'user-edit.html'

    def get_success_url(self):
        return reverse_lazy('account:user-profile', kwargs={'pk': self.object.pk})