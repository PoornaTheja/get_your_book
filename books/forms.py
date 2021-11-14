from django import forms
from comments.models import comment

class search_form(forms.Form):
    search = forms.CharField(max_length=100)


class review_form(forms.ModelForm):
    class Meta:
        model = comment
        fields = ['comment']