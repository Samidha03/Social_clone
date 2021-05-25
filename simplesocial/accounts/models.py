from django.db import models
from django.contrib import auth                                #Built-in authorization tool it contains

# Create your models here.
class User(auth.models.User,auth.models.PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username)    #Where does the username comes from .Thats the attribute that is buit-in that come from user
