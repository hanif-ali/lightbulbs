from django.shortcuts import render
from .forms import RegistrationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse



def register(request):
    """View to both render the registration page and handle registration stuff"""

    if request.method == 'POST':
        form = Registrationform(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Your Account has been created! Edit your Profile Now.')
            return redirect(reverse("edit-profile-page"))  # Profile Edit Page

        else:
            messages.error("Could not create your account. The form is invalid!")
            return redirect(reverse("registration-page"))

    else:
        form = Registrationform()

    return render(request, 'LB/registration.html', {'form':form} )