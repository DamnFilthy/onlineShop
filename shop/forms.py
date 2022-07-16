from django import forms

class RegisterForm(forms.Form):
    name = forms.CharField(label='name', max_length=50)
    email = forms.CharField(label='email', max_length=50)
    phone = forms.CharField(label='phone', max_length=50)
    password = forms.CharField(label='password', max_length=50)

class LoginForm(forms.Form):
    email = forms.CharField(label='email', max_length=50)
    password = forms.CharField(label='password', max_length=50)