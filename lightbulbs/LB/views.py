from django.shortcuts import render
from .forms import RegistrationForm, LoginForm, LBCreationForm, ProposalForm, MessageFrom, EditProfileForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import LBUser
from django.http import HttpResponse
from django.contrib.auth import login, authenticate


def create_user(first_name, last_name, email, username, password, age):
    user = LBUser(first_name=first_name, last_name=last_name, email=email, username=username, age=age)
    user.set_password(password)
    user.save()
    return user



def register(request):
    """View to both render the registration page and handle registration stuff"""

    if request.user.is_authenticated:     # Redirect if already logged in 
        messages.info(request, "You are already logged in.")
        return redirect(reverse("feed"))


    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            username = form.cleaned_data["username"]
            age = form.cleaned_data["age"]
            user = create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password, age=age)
            login(request, user)
            messages.success(request, 'Your Account has been created! Edit your Profile Now.')
            return redirect(reverse("edit-profile"))  # Profile Edit Page

    else:
        form = RegistrationForm()

    return render(request, 'LB/registration.html', {'form':form} )


def homepage(request):
    if request.user.is_authenticated:     # Redirect if already logged in 
        messages.info(request, "You are already logged in.")
        return redirect(reverse("feed"))


    return render(request, "LB/home.html", {})


def login_view(request):
    if request.user.is_authenticated:     # Redirect if already logged in 
        messages.info(request, "You are already logged in.")
        return redirect(reverse("feed"))

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.login(request)
            if user:
                login(request, user)
                return redirect(reverse("feed"))


    else:
        form = LoginForm()

    return render(request, "LB/login.html", {'form':form})


def feed(request):
    pass


def send_proposal(request, id_number):
    pass


def notifications(request):
    pass


def delete_notification(request, id_number):
    pass


def inbox(request):
    pass


def reply(request, id_number):
    pass


def delete_message(request, id_number):
    pass


def idea(request, id_number):
    pass


def profile(request):
    pass


def edit_profile(request):
    pass


def my_ideas(request):
    pass


def create_idea(request, id_number):
    pass


def delete_idea(request, id_number):
    pass


def edit_idea(request, id_number):
    pass


def sent_proposals(request):
    pass


def delete_sent(request, id_number):
    pass


def upvote(request, id_number):
    pass


def downvote(request, id_number):
    pass


def star(request, id_number):
    pass
