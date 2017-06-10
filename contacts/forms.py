from django import forms
from .models import Contacts

class ContactsForm(forms.ModelForm):

    class Meta:
        model = Contacts
        fields = ['nickname','country','phone_number','date_of_br','gender','about', ]
        
