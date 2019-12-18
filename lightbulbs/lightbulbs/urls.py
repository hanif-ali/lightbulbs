"""lightbulbs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import LB.views as LB

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', LB.homepage, name='home-page'),
    path("login", LB.login_view, name='login'),
    path("logout", LB.logout_view, name="logout"),
    path("register", LB.register, name='register'),
    path("feed", LB.Feed.as_view(), name="feed"),
    path("idea/<int:id_number>", LB.Idea.as_view(), name="idea"),
    path("idea/<int:id_number>/send", LB.SendProposal.as_view(), name="send-proposal"),
    path("notifications", LB.Notifications.as_view(), name="notifications"),
    path("notifications/delete/<int:id_number>", LB.DeleteNotification.as_view(), name="delete-notification"),
    path("inbox", LB.Inbox.as_view(), name="inbox"),
    path("inbox/send/<int:id_number>", LB.SendMessage.as_view(), name="send-message"),
    path("inbox/delete/<int:id_number>", LB.DeleteMessage.as_view(), name="delete-message"),
    path("me", LB.Profile.as_view(), name="profile"),
    path("me/edit", LB.EditProfile.as_view(), name="edit-profile"),
    path("me/ideas", LB.my_ideas, name="my-ideas"),
    path("me/ideas/delete/<int:id_number>", LB.DeleteIdea.as_view(), name="delete-idea"),
    path("me/ideas/create", LB.CreateIdea.as_view(), name="create-idea"),
    path("me/ideas/edit/<int:id_number>", LB.EditIdea.as_view(), name="edit-idea"),
    path("me/sent", LB.SentProposals.as_view(), name="sent-proposals"),
    path("me/sent/delete/<int:id_number>", LB.DeleteSentProposal.as_view(), name="delete-sent-proposal"),
    path("upvote/<int:id_number>", LB.upvote, name="upvote"),
    path("downvote/<int:id_number>", LB.downvote, name="downvote"),
    path("star/<int:id_number>", LB.star, name="star"),


]
