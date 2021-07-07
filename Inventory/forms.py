from django import forms

class CreateNewList(forms.Form):
    owner = forms.CharField(label="Owner", max_length=200)
    name = forms.CharField(label="List Name", max_length=200)