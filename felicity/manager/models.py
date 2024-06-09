from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class SelfInfo(models.Model):
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=120)
    state = models.CharField(max_length=32)
    gstin = models.CharField(max_length=32)

    def __str__(self):
        return self.name
    
class Buyer(models.Model):
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=120)
    state = models.CharField(max_length=32)
    gstin = models.CharField(max_length=32)

    def __str__(self):
        return self.name

class Invoice(models.Model):
    seller = models.ForeignKey(SelfInfo, on_delete=models.CASCADE, related_name='invoiceSeller')
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, related_name= 'invoiceBuyer')
    date = models.DateField()

    def __str__(self):
        return str(self.id)

class Challan(models.Model):
    sender = models.ForeignKey(SelfInfo, on_delete=models.CASCADE, related_name='challanSender')
    receiver = models.ForeignKey(Buyer, on_delete=models.CASCADE, related_name='challanReceiver')
    date = models.DateField()

    def __str__(self):
        return str(self.id)

class Entry (models.Model):
    invoicenum = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='invoiceEntry') 
    particulars = models.CharField(max_length=64)
    hsn = models.IntegerField()
    shade = models.CharField(max_length=64)
    challan = models.IntegerField()
    prgnum = models.IntegerField()
    dyeType = models.CharField(max_length=64)
    qty = models.FloatField()
    rate = models.FloatField()

    def __str__(self):
        return str(self.invoicenum)
    
class ChallanEntry(models.Model):
    challanNum = models.ForeignKey(Challan, on_delete=models.CASCADE, related_name='challanEntry') 
    materialName = models.CharField(max_length=64)
    shade = models.CharField(max_length=64)
    dyeingType = models.CharField(max_length=64, blank=True, null=True)
    befQty = models.FloatField(blank=True, null=True)
    aftQty = models.FloatField(blank=True, null=True)
    remark = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return str(self.id)

