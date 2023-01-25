from django import forms

class CreateUser(forms.Form):
    firstname = forms.CharField(label = 'First Name', max_length = 200, required = False)
    lastname  = forms.CharField(label = 'Last Name', max_length = 200, required = False)
    pseudo    = forms.CharField(label = 'Pseudo', max_length = 200)
    password  = forms.CharField(label = 'Password', max_length = 200, widget = forms.PasswordInput)


class CreateAction(forms.Form):
    name   = forms.CharField(label = 'Name', max_length = 200)
    repeat = forms.IntegerField(label = 'Repetition', required = False, min_value = 1)
    ignore = forms.BooleanField()


class CreateParameter(forms.Form):
    key     = forms.CharField(label = 'Name', max_length = 200)
    value   = forms.CharField(label = 'Value', max_length = 10000, required = False)
    comment = forms.CharField(label = 'Comment', max_length = 100)