from .models import *
from django import forms


class SignUpForm(forms.ModelForm):
    class Meta:
        model = RegisteredUsers
        fields = "__all__"
        widgets = {
            "password": forms.PasswordInput(),
        }
