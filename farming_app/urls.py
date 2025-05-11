# from django.contrib import admin
from django.urls import path
from farming_app import views
from .views import add_to_cart, cart_view
from django.contrib.auth.decorators import login_required
# @login_required(login_url='/accounts/login/')

urlpatterns = [
   
    path('',views.home, name='home'),
    path('register/',views.register, name='register'),
    path('login/',views.login, name='login'),
    path('about/',views.about, name='about'),
    path('blog/',views.blog, name='blog'),
    path('contact/',views.contact, name='contact'),
    path('feature/',views.feature, name='feature'),
    path('product/',views.product, name='product'),
    path('testimonial/',views.testimonial, name='testimonial'),
    path('mes/',views.mes, name='mes'),
    path('footer/',views.footer, name='footer'),
    path('base/',views.base, name='base'),
    path('logout/',views.logout, name='logout'),
    path('services/',views.services, name='services'),
    path('farm/',views.farm, name='farm'),
    path('moreproducts/',views.moreproducts, name='moreproducts'),
    path(' moreservices/',views.services1, name='services1'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', cart_view, name='cart_view'),

]