from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

from unfold.admin import ModelAdmin as UnfoldModelAdmin

# Register your models here.
class AccountAdmin(UserAdmin, UnfoldModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active')
    list_display_links = ('email', 'first_name', 'last_name')
    search_fields = ('email', 'username')
    readonly_fields = ('date_joined', 'last_login')
    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'first_name', 'last_name', 'phone_number', 'password1', 'password2')
        }),
    )

admin.site.register(Account, AccountAdmin)
