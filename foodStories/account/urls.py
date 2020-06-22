from django.urls import path
from account.views import RegisterView,LoginView,ChangePasswordView,ChangePasswordDoneView
from django.contrib.auth.views import LogoutView
app_name = 'account'

urlpatterns = [
    path('register', RegisterView.as_view(), name = 'register'),
    path('login', LoginView.as_view(), name = 'login'),
    path('logout', LogoutView.as_view(), name = 'logout'),
    path('change_password/',ChangePasswordView.as_view(), name = 'change-password'),
    path('change_password_done/',ChangePasswordDoneView.as_view(), name = 'change-password-done'),
    # path('reset_password/r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$'')
]