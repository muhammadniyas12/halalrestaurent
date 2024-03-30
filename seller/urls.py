from django.urls import path
from . import views
app_name='seller'
urlpatterns=[
   path('',views.home,name='home'),
   path('signup/',views.signup,name='signup'),

   path('adpdt/',views.adpdt,name='adpdt'),
   path('dashboard/',views.dashboard,name='dashboard'),
   path('viewpdt/',views.viewpdt,name='viewpdt'),
   path('sellerlogin/',views.slogin,name='sellerlogin'),
   path('update/',views.update,name='update'),
   path('deletepdt/<int:pid>',views.deletepdt,name='deletepdt'),
   path('updatepdt/<int:pid>',views.updatepdt,name='updatepdt'),

]

