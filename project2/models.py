from django.conf import settings
from django.db import models

class Profile(models.Model):

    user = models.ForeignKey(settings. AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_pic = models.ImageField( upload_to=f'profile', max_length=250, unique=False)
    created = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.user.username


    def __repr__(self):
        self.user.username