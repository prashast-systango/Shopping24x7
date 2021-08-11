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
from Customer import views as customerViews
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
# from .forms import CustomerLoginForm, MyPasswordChangeForm
from Customer.forms import CustomerLoginForm, MyPasswordChangeForm
from Partner import views as partnerViews

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # path('', views.home),
    path('', customerViews.HomeView.as_view(), name="home"),

    # path('', customerViews.),
    # path('mobile/', customerViews.mobile, name='mobile'),
    # path('mobile/', customerViews.mobile, name='mobile'),
    path('product-detail/<int:pk>', customerViews.ProductDetailView.as_view(), name='product-detail'),
    
    path('mobile/<slug:data>', customerViews.MobileView.as_view(), name='mobiledata'),
    path('mobile/', customerViews.MobileView.as_view(), name='mobile'),
    
    # Customer Log-in 
    path('accounts/login/', auth_views.LoginView.as_view(template_name='customer/login.html', authentication_form=CustomerLoginForm),
     name='login'),

    # customer log-out
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    # change password
    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='customer/passwordchange.html',
     form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'), name='changepassword'),

    path('passwordchangedone/', auth_views.PasswordChangeView.as_view(template_name='customer/passwordchangedone.html'), name='passwordchangedone'),


    # partner home page
    path('partner_home/', partnerViews.PartnerHomeView.as_view(), name='partner-home'),

    # add products url
    path('add_product/', partnerViews.AddProductsView.as_view(), name='product-add'),

    # partner logout
    path('partner_logout/', auth_views.LogoutView.as_view(next_page='/partner_home'), name='partner_logout'),

    # add employee url
    path('add_employee/', partnerViews.AddEmployeeView.as_view(), name='employee-add'),


    path('laptop/', customerViews.LaptopView.as_view(), name='laptop'),
    path('laptop/<slug:data>', customerViews.LaptopView.as_view(), name='laptopdata'),
    
    path('accessories/', customerViews.AccessoryView.as_view(), name='accessories'),

    path('cart/', customerViews.add_to_cart, name='add-to-cart'),
    path('buy/', customerViews.buy_now, name='buy-now'),

    # customer profile
    path('profile/', customerViews.profileView.as_view(), name='profile'),


    path('address/', customerViews.address, name='address'),
    path('orders/', customerViews.orders, name='orders'),
    # path('changepassword/', customerViews.change_password, name='changepassword'),
    # path('login/', customerViews.login, name='login'),
    path('registration/', customerViews.CustomerRegistrationView.as_view(), name='customerregistration'),
    path('checkout/', customerViews.checkout, name='checkout'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
