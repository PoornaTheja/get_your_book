from django import forms

class search_form(forms.Form):
    search = forms.CharField(max_length=100)

class filter_form(forms.Form):
    select_genre = forms.CharField(max_length=100)
    select_author = forms.CharField(max_length=100)