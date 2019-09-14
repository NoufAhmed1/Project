from django import forms
from .models import Item , UserProfil
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username =forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput())

class UserForm(forms.ModelForm):
    username = forms.CharField(help_text=' ')
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields =['username','email','password']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfil
        fields =['mobile']



class addItem(forms.ModelForm):
    picture =forms.ImageField(required=False)
    class Meta:
        model = Item
        fields =['typ','Manufacturer','phonenum','price','city','start_on','picture']

       


