from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label='Username',max_length=30, min_length=3, widget=forms.TextInput(attrs={
        'placeholder':'Username'
    }))
    password = forms.CharField(label='Password',max_length=30, min_length=4, widget=forms.PasswordInput(attrs={
        'placeholder':'Password'
    }))


class ProfileForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username'}), required=False)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'First Name'}), required=False)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Last Name'}), required=False)
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder':'Email'}), required=False)
    
    def save(self, user):
        user.username = self.cleaned_data.get('username')
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.save()
        # return super().save(commit)