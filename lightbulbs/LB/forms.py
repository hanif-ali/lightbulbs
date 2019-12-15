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