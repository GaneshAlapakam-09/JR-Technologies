from django.urls import path

from app1 import views

urlpatterns = [
    path('signin/',views.signin,name='signin'),
    path('',views.dashboard,name='dashboard'),
    path('addCustomer/',views.addCustomer,name='addCustomer'),
    path('listCustomer/',views.listCustomer,name='listCustomer'),
    path('remove/<str:id>',views.remove,name='remove'),
    path('removeEmp/<str:id>',views.remove,name='remove'),
    path('addEmployee/',views.addEmployee,name='addEmployee'),
    path('listEmployee/',views.listEmployee,name='listEmployee'),
    path('addMaterial/',views.addMaterial,name='addMaterial'),
    path('listMaterial/',views.listMaterial,name='listMaterial'),
    path('addInward/',views.addInward,name='addInward'),
    path('listInward/',views.listInward,name='listInward'),
    path('signout/',views.signout,name='signout')
]
