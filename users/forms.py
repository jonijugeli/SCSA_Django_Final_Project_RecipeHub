from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Profile

class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'password1', 'password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone', 'bio']
