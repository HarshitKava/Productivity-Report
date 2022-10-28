from email.policy import default
from django.db import models
from django import forms
from django.conf import settings
from numpy import place

# Create your models here.

class Structure(models.Model):
    StructureName=models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.StructureName

class Staff (models.Model):
    ROLE=(
        ('Site Engineer','Site Engineer'),
        ('Mangement','Mangement'),
        ('Camp Labour Incharge','Camp Labour Incharge'),
        ('Site Labour Incharge','Site Labour Incharge'),
        ('Admin','Admin')
    )
    userid=models.CharField(max_length=200, null=True)
    Name=models.CharField(max_length=200, null=True)
    Role=models.CharField(max_length=200, null=True,choices=ROLE)
    Location=models.CharField(max_length=200, null=True)
    Password=models.CharField(max_length=200, null=True)
    

class Area(models.Model):
    AreaName=[
        ('','None'),
        ('Bhopal','Bhopal'),
        ('SBN','SBN'),
        ('KV','KV'),
        ('DBM','DBM'),
        ('MPZ','MPZ'),
        ('RKP','RKP'),
        ('HBM','HBM'),
        ('ALK','ALK'),
        ('AIIMS','AIIMS'),
        ('Bangalore','Bangalore'),
        ('Casting Yard','Casting Yard'),
        ('Casting Yard QC','Casting Yard QC'),
        ('Casting Yard PM','Casting Yard PM'),   
    ]
    Username=models.CharField(max_length=200, null=True) #ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
    AreaName=models.CharField(max_length=200, null=True,choices=AreaName,default='None')

    def __str__(self):
        return self.AreaName
    

class ContractorDetail(models.Model):
    ContractorName=models.CharField(max_length=200, null=True)
    ContractorNumber=models.IntegerField(null=True)
    
    def __str__(self):
        return str(self.ContractorName)
    

class AddLabour(models.Model):
    LabourCategory=models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.LabourCategory
    



class LabourOfContractor(models.Model):
    ContractorName=models.ForeignKey(ContractorDetail, on_delete=models.CASCADE, null=True)
    LabourCategory=models.ForeignKey('AddLabour', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.LabourCategory)


class SiteEngDay (models.Model):
    Areaname=models.ForeignKey(Area, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now=True,null=True)
    ContractorName=models.ForeignKey('ContractorDetail', on_delete=models.CASCADE, null=True)
    LabourCategory=models.ForeignKey('LabourOfContractor', on_delete=models.CASCADE, null=True)
    StructureName=models.ForeignKey('Structure', on_delete=models.CASCADE, null=True)
    NoLabor=models.IntegerField(null=True)
    def __str__(self):
        return str(self.ContractorName)

class SiteEngNight (models.Model):
    Areaname=models.ForeignKey(Area, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now=True,null=True)
    ContractorName=models.ForeignKey('ContractorDetail', on_delete=models.CASCADE, null=True)
    LabourCategory=models.ForeignKey('LabourOfContractor', on_delete=models.CASCADE, null=True)
    StructureName=models.ForeignKey(Structure,on_delete=models.CASCADE,null=True)
    NoLabor=models.IntegerField(null=True)
    def __str__(self):
        return str(self.ContractorName)

class SLIDay (models.Model):
    Areaname=models.ForeignKey(Area, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now=True,null=True)
    ContractorName=models.ForeignKey('ContractorDetail', on_delete=models.CASCADE, null=True)
    LabourCategory=models.ForeignKey('LabourOfContractor', on_delete=models.CASCADE, null=True)
    NoLabor=models.IntegerField(null=True)
    NoHelp=models.IntegerField(null=True)
    def __str__(self):
        return str(self.ContractorName)

class SLINight (models.Model):
    Areaname=models.ForeignKey(Area, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now=True,null=True)
    ContractorName=models.ForeignKey('ContractorDetail', on_delete=models.CASCADE, null=True)
    LabourCategory=models.ForeignKey('LabourOfContractor', on_delete=models.CASCADE, null=True)
    NoLabor=models.IntegerField(null=True)
    NoHelp=models.IntegerField(null=True)
    def __str__(self):
        return str(self.ContractorName)

class CLIDay (models.Model):
    Areaname=models.ForeignKey(Area, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now=True,null=True)
    ContractorName=models.ForeignKey('ContractorDetail', on_delete=models.CASCADE, null=True)
    LabourCategory=models.ForeignKey('LabourOfContractor', on_delete=models.CASCADE, null=True)
    NoLabor=models.IntegerField(null=True)
    NoHelp=models.IntegerField(null=True)
    def __str__(self):
        return str(self.ContractorName)

class CLINight (models.Model):
    Areaname=models.ForeignKey(Area, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now=True,null=True)
    ContractorName=models.ForeignKey('ContractorDetail', on_delete=models.CASCADE, null=True)
    LabourCategory=models.ForeignKey('LabourOfContractor', on_delete=models.CASCADE, null=True)
    NoLabor=models.IntegerField(null=True)
    NoHelp=models.IntegerField(null=True)
    def __str__(self):
        return str(self.ContractorName)

         

    