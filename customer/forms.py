from django import forms
from customer.models import modelName
from customer.models import libraryModel

class formName(forms.ModelForm):
    class Meta():
        model = modelName
        fields = '__all__'


class libraryForm(forms.ModelForm):
    class Meta():
        model = libraryModel
        fields = '__all__'
