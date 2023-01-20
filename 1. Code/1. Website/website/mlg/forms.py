from django import forms

class CreateUser(forms.Form):
    firstname = forms.CharField(label='First Name', max_length = 200, required=False)
    lastname  = forms.CharField(label='Last Name', max_length = 200, required=False)
    pseudo    = forms.CharField(label='Pseudo', max_length = 200)
    password  = forms.CharField(label='Password', max_length=200, widget=forms.PasswordInput)


class CreateAction(forms.Form):
    name   = forms.CharField(label='Name', max_length=200)
    repeat = forms.IntegerField(label='Repetition', required=False)
    ignore = forms.BooleanField()