from django.db import models

# Create your models here.
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField


class Contacts(models.Model):
    MALE, FEMALE = 'M', 'F'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )

    nickname = models.CharField( max_length=30, null=True)
    country = CountryField(blank_label='Select country', null=True)
    #TODO: Do regex valid
    phone_number = PhoneNumberField(null=True, unique=True)
    about = models.TextField(max_length=200, null=True)
    date_of_br = models.DateField("date of birth", null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=MALE, null=True)


    def __str__(self):
    #TODO: good str
        return self.nickname

Contacts.MALE