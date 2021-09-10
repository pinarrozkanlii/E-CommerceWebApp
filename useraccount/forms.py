from django import forms
from django.contrib.auth.forms import (AuthenticationForm, PasswordResetForm,
                                       SetPasswordForm)
from django.forms.widgets import EmailInput, PasswordInput, TextInput

from .models import UserBase

class UserLoginForm(AuthenticationForm):
    username=forms.CharField(max_length=50)
    password = forms.CharField(widget=PasswordInput)
    email = forms.CharField(widget=EmailInput)
class RegistrationForm(forms.ModelForm):

    user_name = forms.CharField(
        label='Enter Username', min_length=4, max_length=50, help_text='Required')
    email = forms.EmailField(max_length=100, help_text='Required', error_messages={
        'required': 'Sorry, you will need an email'})
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = UserBase
        fields = ('user_name', 'email',)

    def clean_username(self):
        user_name =  self.cleaned_data['user_name'].lower()
        r=UserBase.objects.filter(user_name=user_name)
        if r.count():
            raise forms.ValidationError("Username already exists")
        return user_name

    def clean_password2(self):
        cd=self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords do not match.')
        return cd['password2']


    def clean_email(self):
        email = self.cleaned_data['email']
        if UserBase.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'Please use another Email, that is already taken'
            )
        return email            
