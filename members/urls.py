from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
) 

urlpatterns = [
    path('login/', LoginView.as_view(template_name='members/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='members/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.view_profile, name='view_profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('change-password/', views.change_password, name='change_password'),
    path(
        'reset-password/',
        PasswordResetView.as_view(template_name='members/reset_password.html', 
        email_template_name='members/reset_password_email.html', success_url=reverse_lazy('members:password_reset_done')), 
        name='reset_password'
    ),
    path(
        'reset-password/done/', 
        PasswordResetDoneView.as_view(template_name='members/reset_password_done.html'), 
        name='password_reset_done'
    ),
    path(
        'reset-password/confirm/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(template_name='members/reset_password_confirm.html',
        success_url=reverse_lazy('members:password_reset_complete')),
        name='password_reset_confirm'
    
    ),
    path('reset-password/complete/', PasswordResetCompleteView.as_view(template_name='members/reset_password_complete.html'), name='password_reset_complete'),
]

app_name = "accounts"