from django.forms import ModelForm
from .models import Applications, Contracts, Departments, \
    DocumentsTypes, EducationType, Log, Orders, \
    Passports, Positions, Workers


class NewWorkerForm(ModelForm):
    class Meta:
        model = Workers
        fields = '__all__'


class PassportForm(ModelForm):
    class Meta:
        model = Passports
        fields = '__all__'
