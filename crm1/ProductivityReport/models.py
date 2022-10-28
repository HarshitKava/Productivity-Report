from django.db import models
#import model from other app
from LabourReport.models import *

# Create your models here.

class CategoryOfDeployment(models.Model):
    ActivityName=models.ForeignKey(AddLabour,on_delete=models.CASCADE,null=True)
    CategoryName=models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.CategoryName



class ProductivityReport(models.Model):
    Areaname=models.ForeignKey(Area, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now=True,null=True)
    ContractorName=models.ForeignKey(ContractorDetail, on_delete=models.CASCADE, null=True)
    ActivityName=models.ForeignKey(LabourOfContractor,on_delete=models.CASCADE,null=True)
    ActivityNameBeta=models.ForeignKey(AddLabour,on_delete=models.CASCADE,null=True)
    CategoryName=models.ForeignKey(CategoryOfDeployment,on_delete=models.CASCADE,null=True)
    Deployment=models.IntegerField(null=True,default=1)
    StructureName=models.ForeignKey(Structure,on_delete=models.CASCADE,null=True)
    Length=models.IntegerField(null=True,default=1)
    Breadth=models.IntegerField(null=True,default=1)
    Depth=models.IntegerField(null=True,default=1)
    Quantity=models.IntegerField(null=True,default=1)

class ProductivityNightReport(models.Model):
    Areaname=models.ForeignKey(Area, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now=True,null=True)
    ContractorName=models.ForeignKey(ContractorDetail, on_delete=models.CASCADE, null=True)
    ActivityName=models.ForeignKey(LabourOfContractor,on_delete=models.CASCADE,null=True)
    ActivityNameBeta=models.ForeignKey(AddLabour,on_delete=models.CASCADE,null=True)
    CategoryName=models.ForeignKey(CategoryOfDeployment,on_delete=models.CASCADE,null=True)
    Deployment=models.IntegerField(null=True,default=1)
    StructureName=models.ForeignKey(Structure,on_delete=models.CASCADE,null=True)
    Length=models.IntegerField(null=True,default=1)
    Breadth=models.IntegerField(null=True,default=1)
    Depth=models.IntegerField(null=True,default=1)
    Quantity=models.IntegerField(null=True,default=1)
    