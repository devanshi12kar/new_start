from django.contrib import admin
from.models import Profile
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','profile_pic','created')
    search_feilds= ('user', 'profile_pic')
    ordering=('created',)
