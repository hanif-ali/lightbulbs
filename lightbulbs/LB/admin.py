from django.contrib import admin
from .models import LBUser
from django.contrib.auth.admin import UserAdmin
from .models import LBUser, Lightbulb, Message, Notification, Proposal
from .forms import LBUserChangeForm, LBUserCreationForm

# Register your models here.


@admin.register(LBUser)
class LBUserAdmin(UserAdmin):
    form = LBUserChangeForm
    add_form = LBUserCreationForm
    model = LBUser
    list_display = ['username', 'first_name', 'last_name', 'profession', 'email']
    fieldsets = (
        ("Authentication", {'fields': ('username', 'password')}),
        ("Personal Information", {'fields': ('first_name', 'last_name', 'email', 'description', 'bio', 'profession', 'age')}),
        ("Skills", {'fields':('skills',)}),
        ("Links", {'fields': ('facebook', 'linkedin', 'github')}),

        )

    add_fieldsets = fieldsets[:2]


@admin.register(Lightbulb)
class LightbulbAdmin(admin.ModelAdmin):
    model = Lightbulb
    list_display = ['title', 'creator', 'timestamp']
    add_fieldsets = (
        ("Basic Details", {'fields': ('creator', 'category')}),
        ("Information", {'fields': ('title', 'description')})
    )

    fieldsets = (("Created", {"fields":('timestamp',)}),) + add_fieldsets
    readonly_fields = ["timestamp"]

@admin.register(Proposal)
class ProposalAdmin(admin.ModelAdmin):
    model = Proposal
    list_display = ['lightbulb', 'sender', 'timestamp']
    add_fieldsets = (
        ("Details", {'fields': ('sender', 'lightbulb', 'message')}),
    )
    fieldsets = (("Sent", {'fields': ('timestamp',)}),) + add_fieldsets
    readonly_fields = ["timestamp"]


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    model = Message
    list_display = ['sender', 'receiver', 'timestamp']
    add_fieldsets = (
        ("Data", {'fields': ('sender', 'receiver', 'message')}),
    )
    fieldsets = (("Sent", {'fields': ('timestamp',)}),) + add_fieldsets
    readonly_fields = ["timestamp"]


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    model = Notification
    list_display = ['user', 'message']
    readonly_fields = ["timestamp"]