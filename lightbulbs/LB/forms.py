from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import LBUser
from django.contrib.auth import authenticate


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
    username = forms.CharField(label="Username", max_length=20, min_length=5)
    password = forms.CharField(max_length=30, widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("The username and/or password is invalid!")
        return self.cleaned_data


    def login(self, request):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        return user



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
    bio = forms.TextInput()
    age = forms.NumberInput()
    skills = forms.TextInput()
    contact_number = forms.NumberInput()
    linkedin = forms.URLInput()
    facebook = forms.URLInput()
    github = forms.URLInput()