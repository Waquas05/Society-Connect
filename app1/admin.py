from django.contrib import admin
from .models import Society, Event, CoreMembers, Member, Profile, Heads

# Register your models here.

admin.site.register(Society)

admin.site.register(Event)

admin.site.register(CoreMembers)

admin.site.register(Member)

admin.site.register(Profile)

admin.site.register(Heads)