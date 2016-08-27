from django.contrib import admin
from .models import Usuario


@admin.register(Usuario)
class SportAdmin(admin.ModelAdmin):
    list_display = ('name','surname','email',)