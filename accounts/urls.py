from django.urls import path
from django.conf.urls import url
from . import views
from django.views.static import serve
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from django.conf import settings


urlpatterns = [
    # path('register.html', views.register, name="register"),
    # path('password_reset/', auth_views.PasswordResetView.as_view(success_url=reverse_lazy('users:password_reset_done')), name='password_reset'),
    # path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('password_reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('password_reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),


    # path('accounts/password-reset/', password_reset, {'post_reset_redirect': reverse_lazy('password_reset_done')}, name='password_reset'),
    # path('accounts/password-reset/done/', password_reset_done, name='password_reset_done'),
    # url(r'^(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, {'post_reset_redirect': reverse_lazy('password_reset_complete')}, name='password_reset_confirm'),
    # path('accounts/password-reset/complete/', password_reset_complete, name='password_reset_complete'),
]
