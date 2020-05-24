from django.contrib import admin

# Register your models here.
from apps.usuarios.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('user', 'cel_no', 'birth_date')

admin.site.register(Profile, ProfileAdmin)