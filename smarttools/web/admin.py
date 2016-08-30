from django.contrib import admin
from .models import Competition, Video

"""
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email',)
"""

@admin.register(Competition)
class CompetitionAdmin(admin.ModelAdmin):
    list_display = ('name', 'startingDate', 'deadline',)


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('name', 'state', 'user_email','competition')
