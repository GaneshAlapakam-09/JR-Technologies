from django.db import models

# Create your models here.
from django.db import models

class CustomerMaster(models.Model):
    Customer_Id = models.CharField(max_length=10, primary_key=True, unique=True, editable=False)
    Customer_Name = models.CharField(max_length=100)
    Phone_Number = models.IntegerField()
    Date_of_Birth = models.DateField(auto_now=False, auto_now_add=False)
    Status = models.IntegerField(default=1)

    def save(self, *args, **kwargs):
        if not self.Customer_Id:
            # Generate Customer_Id starting with jr0001
            last_customer = CustomerMaster.objects.order_by('-Customer_Id').first()
            if last_customer:
                last_id = int(last_customer.Customer_Id[2:])  # Extract the numeric part
                new_id = f"JR{last_id + 1:04d}"
            else:
                new_id = "JR0001"
            self.Customer_Id = new_id
        super(CustomerMaster, self).save(*args, **kwargs)


class CustomerDetails(models.Model):
    Customer_Id = models.CharField(max_length=10, primary_key=True, unique=True, editable=False)
    Customer_Name = models.CharField(max_length=100)
    Phone_Number = models.IntegerField()
    Alt_Phone_Number = models.IntegerField()
    Email = models.EmailField(max_length=254)
    Address = models.CharField(max_length=100)
    Customer_Type = models.CharField(max_length=100)
    Date_of_Birth = models.DateField(auto_now=False, auto_now_add=False)
    Status = models.IntegerField(default=1)
    Vehicle_No = models.CharField(max_length=50, unique=True)
    Model = models.CharField(max_length=50)
    Make = models.CharField(max_length=50)
    def save(self, *args, **kwargs):
        if not self.Customer_Id:
            # Generate Customer_Id starting with jr0001
            last_customer = CustomerMaster.objects.order_by('-Customer_Id').first()
            if last_customer:
                last_id = int(last_customer.Customer_Id[2:])  # Extract the numeric part
                new_id = f"JR{last_id + 1:04d}"
            else:
                new_id = "JR0001"
            self.Customer_Id = new_id
        super(CustomerDetails, self).save(*args, **kwargs)


class EmployeeMaster(models.Model):
    Employee_Id = models.CharField(max_length=10, primary_key=True, unique=True, editable=False)
    Employee_Name = models.CharField( max_length=50)
    Phone_Number = models.IntegerField()
    Email = models.CharField(max_length=50)
    Blood_Group = models.CharField(max_length=50)
    Address = models.CharField(max_length=100)
    Date_Of_Joining = models.DateField(auto_now=False, auto_now_add=False)
    Status = models.IntegerField()
    
    def save(self, *args, **kwargs):
        if not self.Employee_Id:
            # Generate Employee_Id starting with jremp0001
            last_employee = EmployeeMaster.objects.order_by('-Employee_Id').first()
            if last_employee:
                last_id = int(last_employee.Employee_Id[2:])  # Extract the numeric part
                new_id = f"JREMP{last_id + 1:04d}"
            else:
                new_id = "JREMP0001"
            self.Employee_Id = new_id
        super(EmployeeMaster, self).save(*args, **kwargs)