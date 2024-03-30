from django.urls import path
from .import views
app_name='customer'
urlpatterns=[
    path('', views.home,name='home'),
    path('signup/', views.signup,name='signup'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('contact/',views.contact,name='contact'),
    path('viewpdt/',views.viewpdt,name='viewpdt'),
    path('cust_login/',views.cust_login,name='cust_login'),
    path('cart/',views.cart,name='cart'),
    path('payment/',views.payment,name='payment'),
    path('add_to_cart/<int:product_id>/',views.add_to_cart,name='add_to_cart'),
    path('cart/',views.cart,name='cart'),
    path('remove_from_cart/<int:product_id>',views.remove_from_cart,name='remove_from_cart'),

]