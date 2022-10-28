from cProfile import label
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django import forms

class SiteEngDayForm(ModelForm):
    class Meta:
        model = SiteEngDay
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['LabourCategory'].queryset = LabourOfContractor.objects.none()

        if 'ContractorName' in self.data:
            try:
                contractor_id = int(self.data.get('ContractorName'))
                print("Cont id",contractor_id)
                self.fields['LabourCategory'].queryset = LabourOfContractor.objects.filter(ContractorName_id=contractor_id).order_by('LabourCategory')
                print(LabourOfContractor.objects.filter(ContractorName_id=contractor_id).order_by('LabourCategory'))
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['LabourCategory'].queryset = self.instance.ContractorName.LabourCategory.order_by('LabourCategory')
        
        

class SiteEngNightForm(ModelForm):
    class Meta:
        model = SiteEngNight
        fields = '__all__' #['ContName','LaborCat','NoLabor','NoHelp']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['LabourCategory'].queryset = LabourOfContractor.objects.none()

        if 'ContractorName' in self.data:
            try:
                contractor_id = int(self.data.get('ContractorName'))
                print("Cont id",contractor_id)
                self.fields['LabourCategory'].queryset = LabourOfContractor.objects.filter(ContractorName_id=contractor_id).order_by('LabourCategory')
                print(LabourOfContractor.objects.filter(ContractorName_id=contractor_id).order_by('LabourCategory'))
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['LabourCategory'].queryset = self.instance.ContractorName.LabourCategory.order_by('LabourCategory')

class SLIDayForm(ModelForm):
    class Meta:
        model = SLIDay
        fields = '__all__' #['ContName','LaborCat','NoLabor','NoHelp']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['LabourCategory'].queryset = LabourOfContractor.objects.none()

        if 'ContractorName' in self.data:
            try:
                contractor_id = int(self.data.get('ContractorName'))
                print("Cont id",contractor_id)
                self.fields['LabourCategory'].queryset = LabourOfContractor.objects.filter(ContractorName_id=contractor_id).order_by('LabourCategory')
                print(LabourOfContractor.objects.filter(ContractorName_id=contractor_id).order_by('LabourCategory'))
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['LabourCategory'].queryset = self.instance.ContractorName.LabourCategory.order_by('LabourCategory')

class SLINightForm(ModelForm):
    class Meta:
        model = SLINight
        fields = '__all__' #['ContName','LaborCat','NoLabor','NoHelp']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['LabourCategory'].queryset = LabourOfContractor.objects.none()

        if 'ContractorName' in self.data:
            try:
                contractor_id = int(self.data.get('ContractorName'))
                print("Cont id",contractor_id)
                self.fields['LabourCategory'].queryset = LabourOfContractor.objects.filter(ContractorName_id=contractor_id).order_by('LabourCategory')
                print(LabourOfContractor.objects.filter(ContractorName_id=contractor_id).order_by('LabourCategory'))
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['LabourCategory'].queryset = self.instance.ContractorName.LabourCategory.order_by('LabourCategory')

class CLIDayForm(ModelForm):
    class Meta:
        model = CLIDay
        fields = '__all__' #['ContName','LaborCat','NoLabor','NoHelp']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['LabourCategory'].queryset = LabourOfContractor.objects.none()

        if 'ContractorName' in self.data:
            try:
                contractor_id = int(self.data.get('ContractorName'))
                print("Cont id",contractor_id)
                self.fields['LabourCategory'].queryset = LabourOfContractor.objects.filter(ContractorName_id=contractor_id).order_by('LabourCategory')
                print(LabourOfContractor.objects.filter(ContractorName_id=contractor_id).order_by('LabourCategory'))
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['LabourCategory'].queryset = self.instance.ContractorName.LabourCategory.order_by('LabourCategory')

class CLINightForm(ModelForm):
    class Meta:
        model = CLINight
        fields = '__all__' #['ContName','LaborCat','NoLabor','NoHelp']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['LabourCategory'].queryset = LabourOfContractor.objects.none()

        if 'ContractorName' in self.data:
            try:
                contractor_id = int(self.data.get('ContractorName'))
                print("Cont id",contractor_id)
                self.fields['LabourCategory'].queryset = LabourOfContractor.objects.filter(ContractorName_id=contractor_id).order_by('LabourCategory')
                print(LabourOfContractor.objects.filter(ContractorName_id=contractor_id).order_by('LabourCategory'))
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['LabourCategory'].queryset = self.instance.ContractorName.LabourCategory.order_by('LabourCategory')


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','groups','password1','password2']

class AddCont(ModelForm):
    class Meta:
        model = ContractorDetail
        fields = '__all__'
        

class Area_Input(ModelForm):
    class Meta:
        model = Area
        fields = ['AreaName','Username']
        labels={
            "AreaName":""
        }
        widgets={
            'AreaName':forms.Select(attrs={'id':'AreaName'}),
        }
class Add_Labour(ModelForm):
    class Meta:
        model = AddLabour
        fields = '__all__'
        

class Add_Lab_To_Contractor(ModelForm):
    class Meta:
        model = LabourOfContractor
        fields = "__all__"

class ResetPasswordForm(forms.Form):
    class Meta:
        model = User
        fields = "__all__"