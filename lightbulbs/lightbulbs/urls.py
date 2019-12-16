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

    path('/', LB.homepage, name='home-page'),
    path("/login", LB.login, name='login'),
    path("/register", LB.register, name='register'),
    path("/feed", LB.feed, name="feed"),
    path("/ideas/send/<int:id_number>", LB.send_proposal, name="send-proposal"),
    path("/notifications", LB.notifications, name="notifications"),
    path("/notifications/delete", LB.delete_notification, name="delete-notification"),
    path("/inbox", LB.inbox, name="inbox"),
    path("/inbox/reply/<int:id_number>", LB.reply, name="reply"),
    path("/inbox/delete/<int:id_number>", LB.delete_message, name="delete-message"),
    path("/idea/<int:id_number>", LB.idea, name="idea"),
    path("/me", LB.profile, name="profile"),
    path("/me/edit", LB.edit_profile, name="edit-profile"),
    path("/me/ideas", LB.my_ideas, name="my-ideas"),
    path("/me/ideas/delete/<int:id_number>", LB.delete_idea, name="delete-idea"),
    path("/me/ideas/create", LB.create_idea, name="create-idea"),
    path("/me/ideas/edit/<int:id_number>", LB.edit_idea, name="edit-idea"),
    path("/me/sent", LB.sent_proposals, name="sent-proposals"),
    path("/me/sent/delete/<int:id_number>", LB.delete_sent, name="delete-sent"),
    path("/upvote/<int:id_number>", LB.upvote, name="upvote"),
    path("/downvote/<int:id_number>", LB.downvote, name="downvote"),
    path("/star/<int:id_number>", LB.star, name="star"),


]
