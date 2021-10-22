from django.contrib.auth.views import LogoutView
from django.urls import path, reverse_lazy

from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('customer/profile/', views.CustomerProfileView.as_view(), name='customer-profile'),
    path('customer/profile-update/', views.CustomerProfileUpdateView.as_view(), name='customer-profile-update'),
    path('customer/login-register/', views.CustomerLoginRegisterView.as_view(), name='customer-login-register'),
    path('customer/code-confirm/', views.CustomerPhoneNumberConfirmView.as_view(), name='customer-code-confirm'),
    path('customer/password-confirm/', views.CustomerPasswordConfirmView.as_view(), name='customer-password-confirm'),
    path('customer/set-password/', views.CustomerSetPasswordView.as_view(), name='customer-set-password'),
    path('customer/change-password/', views.CustomerChangePasswordView.as_view(), name='customer-change-password'),
    path('customer/logout/', views.CustomerLogoutView.as_view(), name='customer-logout'),
    path('serviceprovider/registration/', views.ServiceProviderRegistrationView.as_view(),
         name='service-provider-registration'),
    path('serviceprovider/login/', views.ServiceProviderLoginView.as_view(), name='service-provider-login'),
    path('serviceprovider/profile/', views.ServiceProviderProfileView.as_view(), name='service-provider-profile'),
    path('serviceprovider/change-password/', views.ServiceProviderChangePasswordView.as_view(),
         name='service-provider-change-password'),
    path('serviceprovider/logout/', LogoutView.as_view(next_page=reverse_lazy('accounts:service-provider-login')),
         name='service-provider-logout'),
]
