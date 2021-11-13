from django import forms
from .models import user

# class login_form(forms.Form):
#     username = forms.CharField()
#     password = forms.CharField(
#         widget=forms.PasswordInput
#     )

#     def clean_username(self):
#         u_name = self.cleaned_data.get("username")
#         qs = u.objects.filter(username__iexact = u_name)

#         if not qs.exists():
#             raise forms.ValidationError("User doesn't exists")
#         return u_name

class register_form(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    pswd = forms.CharField(
        label="Password",
        widget=forms.PasswordInput
    )
    # password2 = forms.CharField(
    #     label="Confirm Password",
    #     widget=forms.PasswordInput
    # )

    def signup(self, request, user):
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.pswd = self.cleaned_data['pswd']
        user.save()

    def clean_name(self):
        u_name = self.cleaned_data.get("name")
        qs = user.objects.filter(username__iexact = u_name)

        if qs.exists():
            raise forms.ValidationError("Take other username")
        return u_name

    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = user.objects.filter(username__iexact = email)

        if qs.exists():
            raise forms.ValidationError("This email is already in use")
        return email

    # def clean_password2(self):
    #     passw = self.cleaned_data.get("password1")
    #     passw2 = self.cleaned_data.get("password2")

    #     if passw != passw2:
    #         raise forms.ValidationError("Password mismatch")

    #     return passw2
        