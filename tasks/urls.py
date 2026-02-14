from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

# app_name = 'tasks'
urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='tasks/login.html'), name='login'),
    path('tasklist/', views.tasklist, name='tasklist'),
    path('login/', auth_views.LoginView.as_view(template_name='tasks/login.html'), name='login'),
    path('register/', views.register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('password-change/', auth_views.PasswordChangeView.as_view(template_name='tasks/password_change.html', success_url='/tasklist/'), name='password_change'),
    path('profile/', views.profile_view, name='profile'),

    
    path("complete/<int:pk>/", views.complete_task, name="complete_task"),
    path("delete/<int:pk>/", views.delete_task, name="delete_task"),
]

#Reset related urls
urlpatterns += [
    # 1 email input
    path(
        'password-reset/',
        auth_views.PasswordResetView.as_view(
            template_name='accounts/password_reset.html',
            email_template_name='accounts/password_reset_email.html',
            success_url=reverse_lazy('password_reset_done')
        ),
        name='password_reset'
    ),

    # 2 email sent page
    path(
        'password-reset/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='accounts/password_reset_done.html'
        ),
        name='password_reset_done'
    ),

    # 3 set new password
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='accounts/password_reset_confirm.html',
            success_url=reverse_lazy('password_reset_complete')
        ),
        name='password_reset_confirm'
    ),

    # 4 success page
    path(
        'reset/complete/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='accounts/password_reset_complete.html'
        ),
        name='password_reset_complete'
    ),

]