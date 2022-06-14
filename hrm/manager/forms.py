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


class NewAppForm(ModelForm):
    class Meta:
        model = Applications
        fields = '__all__'


class NewOrderForm(ModelForm):
    class Meta:
        model = Orders
        fields = '__all__'


class NewContractForm(ModelForm):
    class Meta:
        model = Contracts
        fields = '__all__'
