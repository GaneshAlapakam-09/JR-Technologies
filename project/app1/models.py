from django.db import models

# Create your models here.
from django.db import models

class CustomerMaster(models.Model):
    Customer_Id = models.CharField(max_length=10, primary_key=True, unique=True, editable=False)
    Customer_Name = models.CharField(max_length=100)
    Phone_Number = models.CharField(max_length=15)
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
    Phone_Number = models.CharField(max_length=15)
    Alt_Phone_Number = models.CharField(max_length=15)
    Email = models.EmailField(max_length=254)
    Address = models.CharField(max_length=100)
    Customer_Type = models.CharField(max_length=100)
    Date_of_Birth = models.DateField(auto_now=False, auto_now_add=False)
    Status = models.IntegerField(default=1)
    def save(self, *args, **kwargs):
        if not self.Customer_Id:
            # Generate Customer_Id starting with jr0001
            last_customer = CustomerDetails.objects.order_by('-Customer_Id').first()
            if last_customer:
                last_id = int(last_customer.Customer_Id[2:])  # Extract the numeric part
                new_id = f"JR{last_id + 1:04d}"
            else:
                new_id = "JR0001"
            self.Customer_Id = new_id
        super(CustomerDetails, self).save(*args, **kwargs)