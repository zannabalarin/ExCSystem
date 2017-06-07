from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from core.models import Member
from core.models.GearModels import Gear

# Register your models here.



# Replace the option to create users with the option to create members
admin.site.register(Gear)

admin.site.register(Member, UserAdmin)