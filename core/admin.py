from django.contrib import admin
from core.models import *
# Register your models here.

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    pass
