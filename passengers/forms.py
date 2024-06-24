from django import forms
from .models import Passengers

class PassengersForm(forms.ModelForm):
    class Meta:
        model = Passengers
        fields = ['fio_p', 'tep_p', 'dop_inf']
        widgets = {          
            'dop_inf': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Дополнительная информация'}),
        }
