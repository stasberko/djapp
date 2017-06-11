from django import forms
from .models import Contacts
from captcha.fields import CaptchaField

class ContactsForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Contacts
        fields = ['nickname','email','country','phone_number','date_of_br','gender','about', ]
        
