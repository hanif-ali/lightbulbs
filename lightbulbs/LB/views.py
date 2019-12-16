from django.shortcuts import render
from .forms import RegistrationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import LBUser




def register(request):
    """View to both render the registration page and handle registration stuff"""

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Your Account has been created! Edit your Profile Now.')
            return redirect(reverse("edit-profile-page"))  # Profile Edit Page

        else:
            messages.error(request, "Could not create your account. The form is invalid!")
            return redirect(reverse("registration-page"))

    else:
        form = RegistrationForm()

    return render(request, 'LB/registration.html', {'form':form} )


def homepage(request):
    if request.session.get("logged_in"):
        messages.info(request, "You are already logged in.")
        return redirect(reverse("feed"))

    else:
        return render(request, "LB/home.html", {})


def login(request):
    if request.session.get("logged_in"):
        messages.info(request, "You are already logged in.")
        return redirect(reverse("feed"))

    else:
        if request.method == "POST":
            form = LoginForm(request.POST)
            if form.is_valid():
                # Authentication process
                pass
                
            else:
                messages.warning(request, "The username and/or password is incorrect. ")
                return redirect(reverse("login-page"))

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
