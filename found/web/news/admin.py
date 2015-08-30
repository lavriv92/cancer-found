from django.contrib import admin

from .models import Entry


class EntryAdmin(admin.ModelAdmin):
    model = Entry
    list_display = ('title', 'main_admin_image', 'body', 'slug', )
    list_filter = ('project', )
    readonly_fields = ('main_admin_image', )


admin.site.register(Entry, EntryAdmin)
