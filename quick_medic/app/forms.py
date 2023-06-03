from django import forms 
from django.contrib.auth.models import User

class CreateUserForm(forms.ModelForm):
    model = User
    fiels = "__all__"