from django.contrib import admin

from .models import Person, MagicWord

admin.site.register(Person)
admin.site.register(MagicWord)
