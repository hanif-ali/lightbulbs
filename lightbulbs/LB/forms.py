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
    username = forms.CharField(max_length=20, min_length=5)
    password = forms.PasswordInput()


class LBCreationForm(forms.Form):
    category = forms.CharField(max_length=20)
    title = forms.CharField(max_length=50)
    description = forms.TextInput()


class ProposalForm(forms.Form):
    message = forms.TextInput()


class MessageFrom(forms.Form):
    message = forms.TextInput()


class EditProfileForm(forms.Form):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    description = forms.CharField(max_length=30, empty_value=True)
    profession = forms.CharField(max_length=30)
    bio = forms.TextField(empty_value=True)
    age = forms.PositiveSmallIntegerField()
    skills = forms.TextField(empty_value=True)
    contact_number = forms.PositiveIntegerField(empty_value=True)
    linkedin = forms.URLField(empty_value=True)
    facebook = forms.URLField(empty_value=True)
    github = forms.URLField(empty_value=True)