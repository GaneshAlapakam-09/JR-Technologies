from django.urls import path

from app1 import views

urlpatterns = [
    path('',views.signin,name='signin'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('addCustomer/',views.addCustomer,name='addCustomer'),
    path('listCustomer/',views.listCustomer,name='listCustomer'),
    path('remove/<str:id>',views.remove,name='remove'),
    path('signout/',views.signout,name='signout')
]
