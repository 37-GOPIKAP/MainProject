from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import *

class ManagerSignUpForm(UserCreationForm):

    #first_name = forms.CharField(required=True)
    #last_name = forms.CharField(required=True)
    #phone_number = forms.CharField(required=True)
    email=forms.EmailField(required=True)
    

    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_manager = True
        #user.first_name = self.cleaned_data.get('first_name')
        #user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.save()
        schoolmanager = SchoolManager.objects.create(user=user)
        #schoolmanager.phone_number=self.cleaned_data.get('phone_number')
        
        schoolmanager.save()
        return user 