from django.shortcuts import render

from .forms import RegistrationForm
from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.

def getRating(upvotes,downvotes,timestamp):
    from datetime import datetime, timedelta
    from math import log

    
    def getTimePassed(timestamp):
        current_time=datetime.now()
        time_seconds=datetime.timestamp(current_time)
        return time_seconds-timestamp

    def getScore(upvotes,downvotes):
        return upvotes - downvotes

    score = getScore(upvotes, downvotes)
    order = log(max ( abs (score), 1), 10)
    if score > 0:
        sign = 1
    elif score < 0:
        sign = -1
    else:
        sign = 0     

    timepassed=getTimePassed(timestamp)
    rating=round(sign*order+timepassed/45000,7)        

    return rating



def registeruser(request):
    if request.method == 'POST':
        form = Registrationform(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Your Account has been created!')
            return redirect('''add homepage here''')#Hanif add homepage here
    else:
        form = Registrationform()
    return render(request, '''add template name of registration form''', {'form':form} )
