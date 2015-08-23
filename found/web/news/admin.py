from django.contrib import admin

from .models import Entry


class EntryAdmin(admin.ModelAdmin):
    model = Entry
    list_display = ('title', 'body', 'slug', )


admin.site.register(Entry, EntryAdmin)
