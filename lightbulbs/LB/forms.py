from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import LBUser


class LBUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = LBUser
        fields = "__all__"


class LBUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = LBUser
        fields = "__all__"


class RegistrationForm(UserCreationForm):

    class Meta:
        model = LBUser
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        order = fields


class LoginForm(forms.Form):
    pass