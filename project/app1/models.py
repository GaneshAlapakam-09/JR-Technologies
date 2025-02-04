from django.db import models

# Create your models here.

class CustomerMaster(models.Model):
    Customer_Id = models.CharField(max_length=10, primary_key=True, unique=True, editable=False)
    Customer_Name = models.CharField(max_length=100)
    Phone_Number = models.BigIntegerField()
    Date_of_Birth = models.DateField(auto_now=False, auto_now_add=False)
    Status = models.IntegerField(default=1)

    


class CustomerDetails(models.Model):
    Customer_Id = models.CharField(max_length=10, primary_key=True, unique=True, editable=False)
    Customer_Name = models.CharField(max_length=100)
    Phone_Number = models.BigIntegerField()
    Alt_Phone_Number = models.BigIntegerField()
    Email = models.EmailField(max_length=254)
    Address = models.CharField(max_length=100)
    Customer_Type = models.CharField(max_length=100)
    Date_of_Birth = models.DateField(auto_now=False, auto_now_add=False)
    Status = models.IntegerField(default=1)
    Vehicle_No = models.CharField(max_length=55, unique=True)
    Model = models.CharField(max_length=50)
    Make = models.CharField(max_length=50)
    


class EmployeeMaster(models.Model):
    Employee_Id = models.CharField(max_length=10, primary_key=True, unique=True, editable=False)
    Employee_Name = models.CharField( max_length=50)
    Phone_Number = models.BigIntegerField()
    Email = models.CharField(max_length=50)
    Blood_Group = models.CharField(max_length=50)
    Address = models.CharField(max_length=100)
    Date_Of_Joining = models.DateField(auto_now=False, auto_now_add=False)
    Status = models.IntegerField(default=1)



class MaterialMaster(models.Model):
    Material_Id = models.CharField(max_length=10, primary_key=True, unique=True, editable=False)
    Material_Name = models.CharField(max_length=50)
    Material_Make = models.CharField(max_length=50)
    Model = models.CharField(max_length=50)
    Sub_Categories = models.CharField(max_length=50)
    Size = models.CharField(max_length=50)
    Status = models.IntegerField(default=1)
    


class InwardMaster(models.Model):
    Material_Id = models.CharField(max_length=55)
    Inward_Id = models.CharField(primary_key=True,editable=False, max_length=50)
    Batch_Id = models.CharField(unique=True, null=True, max_length=50)
    Vendor_Name = models.CharField(max_length=50)
    Vendor_Mobile = models.BigIntegerField()
    Vendor_GST = models.CharField(max_length=50)
    Cost_Per_Unit = models.CharField(max_length=50)
    Selling_Cost = models.CharField(max_length=50)
    Invoice_Cost = models.CharField(max_length=50)
    Invoice_Quantity = models.IntegerField()
    Status = models.IntegerField(default=1)
    
class InwardDetails(models.Model):
    Material_Id = models.CharField(max_length=50)
    Inward_Id = models.CharField(max_length=50)
    Batch_Id = models.CharField(unique=True, null=True, max_length=50)
    Vendor_Name = models.CharField(max_length=50)
    Vendor_Mobile = models.BigIntegerField()
    Vendor_GST = models.CharField(max_length=50)
    Cost_Per_Unit = models.CharField(max_length=50)
    Selling_Cost = models.CharField(max_length=50)
    Invoice_Cost = models.CharField(max_length=50)
    Invoice_Quantity = models.IntegerField()
    Serial_No = models.CharField(max_length=50)
    Status = models.IntegerField(default=1)



