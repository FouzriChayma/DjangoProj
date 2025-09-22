from django.contrib import admin
from .models import Person

class PersonAdmin(admin.ModelAdmin):
    search_fields = ('email', 'cin', 'username')

admin.site.register(Person, PersonAdmin)
