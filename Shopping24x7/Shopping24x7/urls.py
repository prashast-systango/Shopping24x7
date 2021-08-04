"""Shopping24x7 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from os import name
from django.contrib.auth.forms import AuthenticationForm
from django.urls import path, include
from Partner import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
# from .forms import CustomerLoginForm, MyPasswordChangeForm
from Partner.forms import CustomerLoginForm, MyPasswordChangeForm

urlpatterns = [
    # path('', views.home),
    path('', views.HomeView.as_view(), name="home"),

    # path('', views.),
    # path('mobile/', views.mobile, name='mobile'),
    # path('mobile/', views.mobile, name='mobile'),
    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    
    path('mobile/<slug:data>', views.MobileView.as_view(), name='mobiledata'),
    path('mobile/', views.MobileView.as_view(), name='mobile'),
    
    # Customer Log-in 
    path('accounts/login/', auth_views.LoginView.as_view(template_name='partner/login.html', authentication_form=CustomerLoginForm),
     name='login'),

    # customer log-out
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    # change password
    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='passwordchange.html',
     form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'), name='changepassword'),

    path('passwordchangedone/', auth_views.PasswordChangeView.as_view(template_name='passwordchangedone.html'), name='passwordchangedone'),


    path('laptop/', views.LaptopView.as_view(), name='laptop'),
    path('laptop/<slug:data>', views.LaptopView.as_view(), name='laptopdata'),
    
    path('accessories/', views.AccessoryView.as_view(), name='accessories'),

    path('cart/', views.add_to_cart, name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    # path('changepassword/', views.change_password, name='changepassword'),
    # path('login/', views.login, name='login'),
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
