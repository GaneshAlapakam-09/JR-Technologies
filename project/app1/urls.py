from django.urls import path

from app1 import views

urlpatterns = [
    path('',views.signin,name='signin'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('addCustomer/',views.addCustomer,name='addCustomer'),
    path('listCustomer/',views.listCustomer,name='listCustomer'),
    path('remove/<str:id>',views.remove,name='remove'),
    path('removeEmp/<str:id>',views.remove,name='remove'),
    path('addEmployee/',views.addEmployee,name='addEmployee'),
    path('listEmployee/',views.listEmployee,name='listEmployee'),
    path('signout/',views.signout,name='signout')
]
