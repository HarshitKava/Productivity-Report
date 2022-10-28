from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class CategoryOfDeploymentForm (ModelForm):
    class Meta:
        model = CategoryOfDeployment
        fields = ['ActivityName','CategoryName']#'__all__' 

class StructureForm (ModelForm):
    class Meta:
        model = Structure
        fields = ['StructureName']#'__all__'

class ProductivityReportForm (ModelForm):
    class Meta:
        model = ProductivityReport
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['ActivityName'].queryset = LabourOfContractor.objects.none()
            # self.fields['CategoryName'].queryset = CategoryOfDeployment.objects.none()

            if 'ContractorName' in self.data:
                try:
                    contractor_id = int(self.data.get('ContractorName'))
                    self.fields['ActivityName'].queryset = LabourOfContractor.objects.filter(ContractorName_id=contractor_id).order_by('LabourCategory')
                    
                except (ValueError, TypeError):
                    pass
            elif self.instance.pk:
                self.fields['ActivityName'].queryset = self.instance.ContractorName.ActivityName.order_by('ActivityName')

            # if 'ActivityNameBeta' in self.data:
            #     try:
            #         activity_id = int(self.data.get('ActivityNameBeta'))
            #         self.fields['CategoryName'].queryset = CategoryOfDeployment.objects.filter(ActivityNameBeta=activity_id).order_by('CategoryName')
            #         # self.fields['CategoryName'].queryset = CategoryOfDeployment.objects.filter(ActivityNameBeta_id=activity_id).order_by('CategoryName')
                    
            #     except (ValueError, TypeError):
            #         pass
            # elif self.instance.pk:
            #     self.fields['CategoryName'].queryset = self.instance.ActivityNameBeta.CategoryName.order_by('CategoryName')

class ProductivityNightReportForm (ModelForm):
    class Meta:
        model = ProductivityNightReport
        fields = ['Areaname','ContractorName','ActivityName','ActivityNameBeta','CategoryName','Deployment','StructureName','Length','Breadth','Depth','Quantity']#'__all__'
    
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['ActivityName'].queryset = LabourOfContractor.objects.none()
            # self.fields['CategoryName'].queryset = CategoryOfDeployment.objects.none()

            if 'ContractorName' in self.data:
                try:
                    contractor_id = int(self.data.get('ContractorName'))
                    print("Cont id",contractor_id)
                    self.fields['ActivityName'].queryset = LabourOfContractor.objects.filter(ContractorName_id=contractor_id).order_by('LabourCategory')
                    print(LabourOfContractor.objects.filter(ContractorName_id=contractor_id).order_by('LabourCategory'))
                except (ValueError, TypeError):
                    pass
            elif self.instance.pk:
                self.fields['ActivityName'].queryset = self.instance.ContractorName.ActivityName.order_by('ActivityName')

            # if 'ActivityName' in self.data:
            #     try:
            #         activity_id = int(self.data.get('ActivityName'))
            #         self.fields['CategoryName'].queryset = CategoryOfDeployment.objects.filter(ActivityName_id=activity_id).order_by('CategoryName')
                    
            #     except (ValueError, TypeError):
            #         pass
            # elif self.instance.pk:
            #     self.fields['CategoryName'].queryset = self.instance.ActivityName.CategoryName.order_by('CategoryName')
