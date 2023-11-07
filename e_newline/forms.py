from django import forms
from django.forms import ModelForm
from.models import Dances


#create a form
class DancesForm(ModelForm):
	class Meta:
		model = Dances
		fields = ('name', 'video_id', 'level','steps')
		labels ={
		'name': '',
		'video_id': '',
		'level': '',
		'steps' : '',

		}

		widgets = {
            'name'  :   forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Dance name'}),
            'video_id'  :   forms.TextInput(attrs={'class':'form-control','placeholder': 'Video ID' }),
            'level'  :   forms.Select(attrs={'class':'form-control', 'placeholder': 'Level'}),
            'steps'	 : forms.URLInput(attrs={'class':'form-control', 'placeholder': 'steps-URL'}),
        }
