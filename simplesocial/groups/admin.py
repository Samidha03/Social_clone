from django.contrib import admin
from . import models
# Register your models here.

class GroupMemberInline(admin.TabularInline):     #We use TabularInLine to visit the admin page
    model = models.GroupMember


admin.site.register(models.Group)
