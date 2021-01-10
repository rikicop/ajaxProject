from django import forms
from .models import Contact,Sum

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class SumForm(forms.ModelForm):
    class Meta:
        model = Sum
        fields = ('first', 'second')
        error_messages = {
            'first': {
                'max_digits': ("Ha colocado un número muy largo"),
                'blank' : ("Este Campo es requerido"),
            },
        }



