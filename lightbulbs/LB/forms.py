from django import forms
from .models import LBUser, Lightbulb, Message, Proposal
from django.contrib.auth import authenticate


class RegistrationForm(forms.ModelForm):

    class Meta:
        model = LBUser
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'age']
        order = fields

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['password'].widget = forms.PasswordInput()

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if LBUser.objects.filter(username=username).exists():
            raise forms.ValidationError("This username has already been taken.")

        return username



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



class LBCreationForm(forms.ModelForm):

    class Meta:
        model = Lightbulb
        fields = ["title", "category", "description"]



class ProposalForm(forms.ModelForm):
    lightbulb_id = forms.IntegerField()
    
    class Meta:
        model = Proposal
        fields = ['message']


class MessageForm(forms.ModelForm):
    receiver_id = forms.IntegerField()

    class Meta:
        model = Message
        fields = ['message']
    


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = LBUser
        fields = ['first_name', 'last_name', 'description', 'profession', 'bio', 'age', 'skills',
            'contact_number', 'linkedin', 'facebook', 'github', ]