from django.db import models
class service(models.Model):
    service_icon = models.CharField(max_length = 50)
    service_title = models.CharField(max_length = 50)    
    service_des = models.TextField()
    
class dta(models.Model):
    cost = models.IntegerField()
    cat = models.TextField()
    date_and_time = models.DateField()
    
class incoming_data(models.Model):
    type = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    amount = models.IntegerField()
    recurring = models.BooleanField()
    term = models.CharField(max_length=20)
    endDate = models.DateField()
    new_field = models.CharField(max_length=50, blank=True, null=True)  # New field


class Transaction(models.Model):
    type = models.CharField(max_length=20, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    category = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=255, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)  # Make amount field nullable
    recurring = models.BooleanField(default=False,null=True)
    term = models.CharField(max_length=20, null=True)
    end_date = models.DateField(null=True)


def __str__(self):
        return self.service_title
# Create your models here.
