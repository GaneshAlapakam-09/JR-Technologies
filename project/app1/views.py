from django.shortcuts import render,redirect
from app1.models import CustomerMaster,CustomerDetails,EmployeeMaster,MaterialMaster,InwardMaster,InwardDetails
from django.contrib.auth.models import User
from django.contrib import messages

from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required
from datetime import datetime,date, timedelta

# Create your views here.


# function for login page
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username,password = password)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            messages.info(request,"username and password not match")
            return redirect('signin')
    return render(request,'login.html')


# function for dashboard page
@login_required(login_url='signin')
def dashboard(request):
    noOfCustomer = CustomerDetails.objects.filter(Status=1)
    noOfEmployee = EmployeeMaster.objects.filter(Status=1)
    noOfMaterial = MaterialMaster.objects.all()
    noOfInwards = InwardMaster.objects.all()
    context= {'totalCustomer':noOfCustomer, 'totalEmployee':noOfEmployee,'totalMaterial':noOfMaterial,'totalInward':noOfInwards}
    return render(request,'index.html',context)
    # return render(request,'index.html')

# function for addCustomer page
@login_required(login_url='signin')
def addCustomer(request):
    if request.method=="POST":
        name = request.POST['name']
        phone = request.POST['phone']
        altPhone = request.POST['alt-phone']
        email = request.POST['email']
        address = request.POST['address']
        customerType = request.POST['customer-type']
        vehecleNo = request.POST['vehicle-no']
        model = request.POST['model']
        make = request.POST['make']
        dateOfBirth = request.POST['dob']
        htmlDob =datetime.strptime(dateOfBirth, "%Y-%m-%d")
        age = datetime.today()-htmlDob
        limit = timedelta(days = 6574)
        last_customer = CustomerMaster.objects.order_by('-Customer_Id').first()
        if last_customer:
            last_id = int(last_customer.Customer_Id[2:])  # Extract the numeric part
            new_id = f"JR{last_id + 1:04d}"
        else:
            new_id = "JR0001"
        data = CustomerDetails.objects.all()
        for num in data:
            if num.Vehicle_No == vehecleNo:
                messages.info(request,'Vehicle Number Already exists')
                return redirect('addCustomer')  
        if limit < age:
            CustomerMaster.objects.create(Customer_Id=new_id,Customer_Name=name,Phone_Number=phone,Date_of_Birth=dateOfBirth)
            CustomerDetails.objects.create(Customer_Id=new_id,Customer_Name=name,Phone_Number=phone,Alt_Phone_Number=altPhone,Address=address,Customer_Type=customerType,Email=email,Date_of_Birth=dateOfBirth,Vehicle_No=vehecleNo,Model=model,Make=make)
            messages.info(request,'Form submitted sucessfully!')
            return redirect('addCustomer')
        else:
            messages.info(request,"Customer age should be 18+")
            return render(request, 'add-customer.html')
    last_customer = CustomerMaster.objects.order_by('-Customer_Id').first()
    if last_customer:
        last_id = int(last_customer.Customer_Id[2:])  # Extract the numeric part
        new_id = f"JR{last_id + 1:04d}"
    else:
        new_id = "JR0001"
    context = {'data':new_id}
    return render(request, 'add-customer.html',context)



# function for addEmployee page
@login_required(login_url='signin')
def addEmployee(request):
    if request.method=="POST":
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        bloodGroup = request.POST['blood_group']
        address = request.POST['address']
        dateOfJoining = request.POST['doj']
        last_employee = EmployeeMaster.objects.order_by('-Employee_Id').first()
        if last_employee:
            last_id = int(last_employee.Employee_Id[5:])  # Extract the numeric part
            new_id = f"JREMP{last_id + 1:04d}"
        else:
            new_id = "JREMP0001"

        messages.info(request,'Form submitted sucessfully!')
        EmployeeMaster.objects.create(Employee_Id=new_id,Employee_Name = name, Phone_Number = phone, Email = email, Blood_Group = bloodGroup, Date_Of_Joining = dateOfJoining, Address = address)
        return redirect('addEmployee')
    last_employee = EmployeeMaster.objects.order_by('-Employee_Id').first()
    if last_employee:
        last_id = int(last_employee.Employee_Id[5:])  # Extract the numeric part
        new_id = f"JREMP{last_id + 1:04d}"
    else:
        new_id = "JREMP0001"
    context={'data':new_id}
    return render(request, 'add-employee.html',context)



# function for listCustomer page
@login_required(login_url='signin')
def listCustomer(request):
    data = CustomerDetails.objects.filter(Status=1)
    context={'data':data}
    return render(request,'list-customer.html',context)


# function for listEmployee page
@login_required(login_url='signin')
def listEmployee(request):
    data = EmployeeMaster.objects.filter(Status=1)
    context={'data':data}
    return render(request,'list-employee.html',context)


# function for addMeterial page
@login_required(login_url='signin')
def addMaterial(request):
    if request.method == 'POST':
        materialName = request.POST['name']
        materialMake = request.POST['make']
        model = request.POST['model']
        subCategories = request.POST['sub-categories']
        size = request.POST['size']
        # Generate Material_Id starting with jremp0001
        last_material = MaterialMaster.objects.order_by('-Material_Id').first()
        if last_material:
            last_id = int(last_material.Material_Id[3:])  # Extract the numeric part
            new_id = f"MAT{last_id + 1:04d}"
        else:
            new_id = "MAT0001"

        messages.info(request,'Form Submitted Sucessfully')
        MaterialMaster.objects.create(Material_Id=new_id,Material_Name = materialName, Material_Make = materialMake, Model = model, Sub_Categories = subCategories, Size = size)
        return redirect('addMaterial')
    # Generate Material_Id starting with jremp0001 and display in front-end
    last_material = MaterialMaster.objects.order_by('-Material_Id').first()
    if last_material:
        last_id = int(last_material.Material_Id[3:])  # Extract the numeric part
        new_id = f"MAT{last_id + 1:04d}"
    else:
        new_id = "MAT0001"
    context={'data':new_id}
    return render(request,'add-material.html',context)


# function for listEmployee page
@login_required(login_url='signin')
def listMaterial(request):
    data = MaterialMaster.objects.all()
    context={'data':data}
    return render(request,'list-material.html',context)
    



# function for remove customer page
@login_required(login_url='signin')
def remove(request,id):
    CustomerDetails.objects.filter(Customer_Id = id).update(Status=0)
    CustomerMaster.objects.filter(Customer_Id = id).update(Status=0)
    return redirect('listCustomer')

def removeEmp(request,id):
    EmployeeMaster.objects.filter(Employee_Id = id).update(Status=0)
    return redirect('listEmployee')

# function for logout page
def signout(request):
    logout(request)
    return redirect('signin')



# function for addInward page
@login_required(login_url='signin')
def addInward(request):
    if request.method == 'POST' and request.POST.get('material_id'):
        id=request.POST['material_id']
        material = MaterialMaster.objects.filter(Material_Id = id)
        last_batch = InwardMaster.objects.order_by('-Batch_Id').first()
        if last_batch:
            last_id = int(last_batch.Batch_Id[3:])  # Extract the numeric part
            new_batch_id = f"BAT{last_id + 1:04d}"
        else:
            new_batch_id = "BAT0001"
        context = {'filtered':material,'batchId':new_batch_id}
        return render(request,'add-inward.html',context)


    if request.method == 'POST':
        materialId=request.POST.get('materialId')
        vendorName = request.POST['vendor-name']
        vendorMobile = request.POST['vendor-mobile']
        vendorGst = request.POST['vendor-gst']
        costPerUnit = request.POST['cost-per-unit']
        sellingCost = request.POST['selling-cost']
        invoiceCost = request.POST['invoice-cost']
        invoiceQuantity = request.POST['invoice-quantity']
        serialNo = request.POST['serial-number']
        splitSerialNo = serialNo.split(',')

        material=MaterialMaster.objects.filter(Status = 1)
        for id in material:
            if id != materialId:
                messages.info(request,"Wrong Material ID")
                return redirect('addInward')

        # for creating new batch Id 
        last_batch = InwardMaster.objects.order_by('-Batch_Id').first()
        if last_batch:
            last_id = int(last_batch.Batch_Id[3:])  # Extract the numeric part
            new_batch_id = f"BAT{last_id + 1:04d}"
        else:
            new_batch_id = "BAT0001"

        

        
        # for creating new Inward Id 
        last_inward = InwardMaster.objects.order_by('-Inward_Id').first()
        if last_inward:
            last_id = int(last_inward.Inward_Id[3:])  # Extract the numeric part
            new_inward_id = f"INW{last_id + 1:04d}"
        else:
            new_inward_id = "INW0001"
        
        InwardMaster.objects.create(Material_Id = materialId, Inward_Id = new_inward_id,Batch_Id=new_batch_id, Vendor_Name = vendorName, Vendor_Mobile = vendorMobile, Vendor_GST = vendorGst, Cost_Per_Unit = costPerUnit, Selling_Cost = sellingCost, Invoice_Cost = invoiceCost, Invoice_Quantity = invoiceQuantity)

        for num in splitSerialNo:
            InwardDetails.objects.create(Material_Id = materialId, Inward_Id = new_inward_id,Batch_Id=new_batch_id, Vendor_Name = vendorName, Vendor_Mobile = vendorMobile, Vendor_GST = vendorGst, Cost_Per_Unit = costPerUnit, Selling_Cost = sellingCost, Invoice_Cost = invoiceCost, Invoice_Quantity = invoiceQuantity, Serial_No = num)
        messages.info(request,'Form Submitted Sucessfully')
        return redirect('addInward')
    materials = MaterialMaster.objects.filter(Status=1)
    context = {'data':materials}
    return render(request,'add-inward.html',context)



# function for listInward page
@login_required(login_url='signin')
def listInward(request):
    data = InwardDetails.objects.filter(Status=1)
    context={'data':data}
    return render(request,'list-inward.html',context)

