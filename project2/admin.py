from django.contrib import admin
from.models import Profile
from.models import New_profile
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','profile_pic','created')
    search_feilds= ('user', 'profile_pic')
    ordering=('created',)

@admin.register(New_profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','profile_pic','created')
    search_feilds= ('user', 'profile_pic')
    ordering=('created',)

