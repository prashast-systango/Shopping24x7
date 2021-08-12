from django.contrib import admin
from os import name
from django.contrib.auth.forms import AuthenticationForm
from django.urls import path, include
from Customer import views as customerViews
from Partner import views as partnerViews
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from Customer.forms import CustomerLoginForm, MyPasswordChangeForm

urlpatterns = [
    path('admin/', admin.site.urls),
    
    
    path('', customerViews.HomeView.as_view(), name="home"),

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


    # PARTNER URL's

    # partner home page
    path('partner_home/', partnerViews.PartnerHomeView.as_view(), name='partner-home'),

    # add products url
    path('add_product/', partnerViews.AddProductsView.as_view(), name='product-add'),

    # partner logout
    path('partner_logout/', auth_views.LogoutView.as_view(next_page='/partner_home'), name='partner_logout'),

    # add employee url
    path('add_employee/', partnerViews.AddEmployeeView.as_view(), name='employee-add'),

    # all products list
    path('all_products/', partnerViews.ProductListView.as_view(), name='products-all'),

    # edit products details form url
    path('edit_products/<str:pk>/', partnerViews.editProductDetails, name='products-edit'),

    # products delete form url
    path('delete_product/<str:pk>/', partnerViews.deleteProduct, name='products-delete'),

    # all employees list
    path('all_employees/', partnerViews.EmployeeListView.as_view(), name='employees-all'),

    # edit products details form url
    path('edit_employee/<str:pk>/', partnerViews.editEmployeeDetails, name='employees-edit'),

    # products delete form url
    path('delete_employee/<str:pk>/', partnerViews.deleteEmployee, name='employees-delete'),


    # add coupons url
    path('add_coupon/', partnerViews.AddCouponsView.as_view(), name='coupon-add'),

    # all employees list
    path('all_coupons/', partnerViews.CouponListView.as_view(), name='coupons-all'),


    path('laptop/', customerViews.LaptopView.as_view(), name='laptop'),
    path('laptop/<slug:data>', customerViews.LaptopView.as_view(), name='laptopdata'),
    
    path('accessories/', customerViews.AccessoryView.as_view(), name='accessories'),

    path('cart/', customerViews.add_to_cart, name='add-to-cart'),
    path('buy/', customerViews.buy_now, name='buy-now'),

    # customer profile
    path('profile/', customerViews.profileView.as_view(), name='profile'),


    path('address/', customerViews.address, name='address'),
    path('orders/', customerViews.orders, name='orders'),
    path('registration/', customerViews.CustomerRegistrationView.as_view(), name='customerregistration'),
    path('checkout/', customerViews.checkout, name='checkout'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
