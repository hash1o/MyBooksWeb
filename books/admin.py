from django.contrib import admin
from .models import MemoBook,Profile,User

from books.forms import UserCreationForm
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
 
 
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
 
 
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password',)}),
        (None, {'fields': ('is_active', 'is_admin',)}),
    )
 
    list_display = ('username', 'email', 'is_active',)
    list_filter = ()
    ordering = ()
    filter_horizontal = ()
 
    add_fieldsets = (
        (None, {'fields': ('username', 'email', 'is_active',)}),
    )
 
    add_form = UserCreationForm
 
    inlines = (ProfileInline,)
 
admin.site.register(MemoBook)
admin.site.register(User, CustomUserAdmin)
admin.site.unregister(Group)