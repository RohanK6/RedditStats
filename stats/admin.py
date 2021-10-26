from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from stats.models import Account
# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'reddit_username', 'date_joined', 'last_login', 'is_admin')
    search_fields = ('email', 'username', 'reddit_username')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)