from django.contrib import admin
from .models import LBUser
from django.contrib.auth.admin import UserAdmin
from .models import LBUser
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

    add_fieldsets = fieldsets