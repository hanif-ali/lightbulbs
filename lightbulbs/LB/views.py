from django.shortcuts import render
from .forms import RegistrationForm, LoginForm, LBCreationForm, ProposalForm, MessageForm, EditProfileForm
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from .models import LBUser
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

# Import models
from .models import LBUser, Lightbulb, Message, Notification, Proposal

# For class based Views
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def create_user(first_name, last_name, email, username, password, age):
    user = LBUser(first_name=first_name, last_name=last_name, email=email, username=username, age=age)
    user.set_password(password)
    user.save()
    return user



def register(request):
    """View to both render the registration page and handle registration stuff"""

    if request.user.is_authenticated:     # Redirect if already logged in 
        messages.info(request, "You are already logged in.")
        return redirect(reverse_lazy("feed"))


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
            return redirect(reverse_lazy("edit-profile"))  # Profile Edit Page

    else:
        form = RegistrationForm()

    return render(request, 'LB/registration.html', {'form':form} )


def homepage(request):
    if request.user.is_authenticated:     # Redirect if already logged in 
        messages.info(request, "You are already logged in.")
        return redirect(reverse_lazy("feed"))


    return render(request, "LB/home.html", {})


def login_view(request):
    if request.user.is_authenticated:     # Redirect if already logged in 
        messages.info(request, "You are already logged in.")
        return redirect(reverse_lazy("feed"))

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.login(request)
            if user:
                login(request, user)
                return redirect(reverse_lazy("feed"))


    else:
        form = LoginForm()

    return render(request, "LB/login.html", {'form':form})


def logout_view(request):
    logout(request)
    messages.success(request, "Logged Out Successfully")
    return redirect(reverse_lazy("login"))



class Feed(ListView, LoginRequiredMixin):
    model = Lightbulb
    template_name = 'LB/feed.html'
    context_object_name = 'ideas'
    ordering = ['-rating']
    paginate_by = 6


    def post(self, *args, **kwargs):
        query = self.request.POST.get("query")
        if query:
            object_list = self.model.objects.filter(title__icontains = query)
        else:
            object_list = self.model.objects.all()

        return render(self.request, "LB/feed.html", {"ideas": object_list})



class Idea(DetailView, LoginRequiredMixin): 
    model = Lightbulb
    template_name = 'LB/idea.html'
    context_object_name = "idea"
    pk_url_kwarg = "id_number"


class SendProposal(LoginRequiredMixin, FormView):
    template_name = "LB/send_proposal.html"
    form_class = ProposalForm

    def get(self, *args, **kwargs):
        id_number = kwargs["id_number"]
        lightbulb = Lightbulb.objects.get(id=id_number)
        form = ProposalForm({"lightbulb_id": lightbulb.id})
        return render(self.request, self.template_name, locals())

    def form_invalid(self, form, *args, **kwargs):
        print(form.errors)
        return HttpResponse("Inavlid form")

    def form_valid(self, form):
        print("Validating Right Now")
        proposal = form.save(commit=False)
        proposal.lightbulb = Lightbulb.objects.get(id=form.cleaned_data['lightbulb_id'])
        proposal.sender = self.request.user
        proposal.save()
        messages.success(self.request, "Your Proposal has been sent.")
        return redirect(reverse_lazy("feed"))



class Notifications(LoginRequiredMixin, ListView):
    template_name = "LB/notifications.html"
    context_object_name = "notifications"

    def get_queryset(self):
        queryset = Notification.objects.filter(user=self.request.user)
        return queryset


class DeleteNotification(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Notification
    pk_url_kwarg = "id_number"
    
    def test_func(self):
        self.notification = self.get_object()
        if self.notification.user == self.request.user:
            return True
        return False

    def get(self, *args, **kwargs):
        self.notification.delete()
        return JsonResponse({"success": True})
    


class Inbox(LoginRequiredMixin, ListView):
    model = Message
    template_name = "LB/inbox.html"
    context_object_name = "inbox_messages"

    def get_queryset(self):
        queryset = Message.objects.filter(receiver=self.request.user)
        return queryset


class DeleteMessage(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Message
    pk_url_kwarg = "id_number"
    success_url = reverse_lazy("inbox")

    
    def test_func(self):
        self.message = self.get_object()
        if self.message.receiver == self.request.user:
            return True
        return False

    def get(self, *args, **kwargs):
        messages.success(self.request, "The message was deleted.")
        self.message.delete()
        return redirect(self.success_url)



class SendMessage(LoginRequiredMixin, FormView):
    template_name = "LB/send_message.html"
    form_class = MessageForm

    def get(self, *args, **kwargs):
        id_number = kwargs["id_number"]
        receiver = LBUser.objects.get(id=id_number)
        form = MessageForm({"receiver_id": receiver.id})
        return render(self.request, self.template_name, locals())


    def form_invalid(self, form, *args, **kwargs):
        print(form.errors)
        return HttpResponse("Inavlid form")


    def form_valid(self, form):
        message = form.save(commit=False)
        message.sender = self.request.user
        message.receiver = LBUser.objects.get(id=form.cleaned_data['receiver_id'])
        message.save()
        messages.success(self.request, "Message Sent")
        return redirect(reverse_lazy("inbox"))



class MyIdeas(ListView, LoginRequiredMixin):
    def get_queryset(self):
        queryset = Lightbulb.objects.filter(creator=self.request.user)
        return queryset
        
    template_name = 'LB/my_ideas.html'
    context_object_name = 'ideas'
    paginate_by = 6



class StarredIdeas(ListView, LoginRequiredMixin):
    def get_queryset(self):
        queryset = self.request.user.stars.all()
        return queryset
        
    template_name = 'LB/starred_ideas.html'
    context_object_name = 'ideas'
    paginate_by = 6



class CreateIdea(LoginRequiredMixin, CreateView):
    template_name = "LB/feed.html"
    form_class = LBCreationForm

    def form_valid(self, form):
        idea = form.save(commit=False)
        idea.creator = self.request.user
        idea.save()
        messages.success(self.request, "The Lightbulb was created successfully")
        return redirect(idea.get_absolute_url())



class DeleteIdea(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Lightbulb
    success_message = "The Lightbulb was removed successfully"
    pk_url_kwarg = "id_number"
    success_url = reverse_lazy("my-ideas")

    def test_func(self):
        idea = self.get_object()
        if self.request.user == idea.creator:
            return True
        return False
    
    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

    def delete(self, *args, **kwargs):
        messages.success(self.request, self.success_message)
        super(DeleteIdea, self).delete(*args, **kwargs)
        return redirect(self.success_url)


class EditIdea(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "LB/editidea.html"
    model = Lightbulb
    pk_url_kwarg = "id_number"
    fields = ["title", "description", "category"]
    context_object_name = "idea"

    def test_func(self):
        idea = self.get_object()
        if idea.creator == self.request.user:
            return True
        return False


class SentProposals(LoginRequiredMixin, ListView):
    template_name = "LB/sent_proposals.html"
    context_object_name = "proposals"

    def get_queryset(self):
        queryset = Proposal.objects.filter(sender=self.request.user)
        return queryset



class DeleteSentProposal(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Proposal
    pk_url_kwarg = "id_number"
    success_url = reverse_lazy("sent-proposals")

    
    def test_func(self):
        self.proposal = self.get_object()
        if self.proposal.sender == self.request.user:
            return True
        return False

    def get(self, *args, **kwargs):
        messages.warning(self.request, "The proposal was deleted.")
        self.proposal.delete()
        return redirect(self.success_url)


@login_required(login_url=reverse_lazy("login"))
def upvote(request, id_number):
    idea = Lightbulb.objects.get(id=id_number)
    if request.user in idea.upvoters.all():
        idea.upvoters.remove(request.user)
        idea.save()
        return JsonResponse({"status": "unupvoted"})
    else:
        idea.upvoters.add(request.user)
        idea.save()
        return JsonResponse({"status": "upvoted"})


@login_required(login_url=reverse_lazy("login"))
def downvote(request, id_number):
    idea = Lightbulb.objects.get(id=id_number)
    if request.user in idea.downvoters.all():
        idea.downvoters.remove(request.user)
        idea.save()
        return JsonResponse({"status": "undownvoted"})
    else:
        idea.downvoters.add(request.user)
        idea.save()
        return JsonResponse({"status": "downvoted"})



@login_required(login_url=reverse_lazy("login"))
def star(request, id_number):
    idea = Lightbulb.objects.get(id=id_number)
    if request.user in idea.starrers.all():
        idea.starrers.remove(request.user)
        idea.save()
        return JsonResponse({"status": "unstarred"})
    else:
        idea.starrers.add(request.user)
        idea.save()
        return JsonResponse({"status": "starred"})

from .models import LBUser
from django.views.generic import DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class Profile(DetailView):
    template_name = 'LB/profile.html'
    context_object_name = "data"

    def get_object(self):
        return get_object_or_404(LBUser, id=self.request.user.id)

    def get_context_data(self, **kwargs):
        context = super(Profile, self).get_context_data(**kwargs)
        context['self_profile'] = True
        return context


class UserProfile(DetailView):
    model = LBUser
    template_name = 'LB/profile.html'
    context_object_name = "data"
    pk_url_kwarg = "id_number"

    def get_context_data(self, **kwargs):
        context = super(UserProfile, self).get_context_data(**kwargs)
        context['self_profile'] = False
        return context



class EditProfile(LoginRequiredMixin, UpdateView):
    form = EditProfileForm
    template_name = 'LB/edit_profile.html'
    fields = ['username','description', 'first_name','last_name', 'email','age','contact_number','profession','bio', 'skills', 'linkedin', 'facebook', 'github']
    success_url = reverse_lazy("profile")

    def get_object(self):
        return get_object_or_404(LBUser, id=self.request.user.id)
