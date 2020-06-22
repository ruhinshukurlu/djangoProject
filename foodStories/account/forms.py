from django.contrib.auth.forms import UserCreationForm, UserChangeForm,AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email',)

class RegisterForm(UserCreationForm):
    password1 = forms.CharField(widget = forms.PasswordInput(attrs = {
       'class' : 'form-control',
       'placeholder' : 'Password' 
    }), required=True)
    password2 = forms.CharField(widget = forms.PasswordInput(attrs = {
       'class' : 'form-control',
       'placeholder' : 'Confirm Password' 
    }), required=True)

    class Meta:
        model = User
        fields = ('first_name','last_name','username','email','password1','password2',)

        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder' : 'First Name',
                }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder' : 'Last Name',
                }),
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder' : 'Username',
                }),
            'email' : forms.EmailInput(attrs = {
                'class' : 'form-control',
                'placeholder' : 'Email'
            }),
        }

class LoginForm(AuthenticationForm):
    username = forms.EmailField(widget = forms.TextInput(attrs = {
        'placeholder' : 'Email',
        'class' : 'form-control',
    }))
    password = forms.CharField(widget = forms.PasswordInput(attrs = {
        'placeholder' : 'Password',
        'class' : 'form-control',
    }))


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(widget = forms.PasswordInput(attrs = {
        'class' : 'form-control',
        'placeholder' : 'Old password'
    }), required=True)

    new_password1 = forms.CharField(widget = forms.PasswordInput(attrs = {
        'class' : 'form-control',
        'placeholder' : 'New password'
    }), required=True)

    new_password2 = forms.CharField(widget = forms.PasswordInput(attrs = {
        'class' : 'form-control',
        'placeholder' : 'Re-enter new password'
    }), required=True)

class ResetPasswordForm(PasswordResetForm):
    email = forms.EmailField(widget = forms.EmailInput(attrs = {
       'placeholder' : 'Email',
       'class' : 'form-control' 
    }), required=True)

class SetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(widget = forms.PasswordInput(attrs = {
        'placeholder' : 'New Password',
        'class' : 'form-control'
    }), required=True)

    new_password2 = forms.CharField(widget = forms.PasswordInput(attrs = {
        'placeholder' : 'Re-enter New Password',
        'class' : 'form-control'
    }), required=True)