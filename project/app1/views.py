from django.shortcuts import render,redirect
from app1.models import CustomerMaster,CustomerDetails
from django.contrib.auth.models import User
from django.contrib import messages

from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required
from datetime import datetime,date, timedelta

# Create your views here.

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username,password = password)
        print(user)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            messages.info(request,"username and password not match")
            return redirect('signin')
    return render(request,'login.html')

@login_required(login_url='signin')
def dashboard(request):
    noOfCustomer = CustomerDetails.objects.filter(Status=1)
    context= {'total':noOfCustomer}
    return render(request,'index.html',context)
    # return render(request,'index.html')

@login_required(login_url='signin')
def addCustomer(request):
    if request.method=="POST":
        name = request.POST['name']
        phone = request.POST['phone']
        altPhone = request.POST['alt-phone']
        email = request.POST['email']
        address = request.POST['address']
        customerType = request.POST['customer-type']
        dateOfBirth = request.POST['dob']
        htmlDob =datetime.strptime(dateOfBirth, "%Y-%m-%d")
        age = datetime.today()-htmlDob
        limit = timedelta(days = 6574)
        if limit < age:
            print("age limit will be added if needed")
            CustomerMaster.objects.create(Customer_Name=name,Phone_Number=phone,Date_of_Birth=dateOfBirth)
            CustomerDetails.objects.create(Customer_Name=name,Phone_Number=phone,Alt_Phone_Number=altPhone,Address=address,Customer_Type=customerType,Email=email,Date_of_Birth=dateOfBirth)
            messages.info(request,'Form submitted sucessfully!')
            return redirect('addCustomer')
        else:
            messages.info(request,"Your age should be 18+")
            return render(request, 'add-customer.html')
    return render(request, 'add-customer.html')

@login_required(login_url='signin')
def listCustomer(request):
    data = CustomerDetails.objects.filter(Status=1)
    context={'data':data}
    return render(request,'list-customer.html',context)

@login_required(login_url='signin')
def remove(request,id):
    CustomerDetails.objects.filter(Customer_Id = id).update(Status=0)
    CustomerMaster.objects.filter(Customer_Id = id).update(Status=0)
    return redirect('listCustomer')


def signout(request):
    logout(request)
    return redirect('signin')