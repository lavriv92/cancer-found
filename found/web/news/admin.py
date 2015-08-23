from django.contrib import admin

from .models import Entry


class EntryAdmin(admin.ModelAdmin):
    model = Entry


admin.site.register(Entry, EntryAdmin)
