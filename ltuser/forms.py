from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)
    repassword = forms.CharField(widget=forms.PasswordInput)
    email    = forms.EmailField()
    class Meta:
        model = User
        fields = ("username","password","email")

class LoginForm(forms.Form):
    username =  forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)
