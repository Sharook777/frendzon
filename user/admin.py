from django.contrib import admin

from .models import Users
class UserAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'mail_id', 'username','phone_no']
    class Meta:
        model = Users

admin.site.register(Users, UserAdmin)