from django.contrib import admin

from .models import MemeberGroup, Memeber, Document, VolonteerTask


class MemeberGroupAdmin(admin.ModelAdmin):
    model = MemeberGroup
    list_display = ('name', )


class MemeberAdmin(admin.ModelAdmin):
    model = Memeber
    list_display = ('full_name', )


class DocumentAdmin(admin.ModelAdmin):
    model = Document
    list_display = ('name', )


class VolonteerTaskAdmin(admin.ModelAdmin):
    list_display = ('title', )

admin.site.register(MemeberGroup, MemeberGroupAdmin)
admin.site.register(Memeber, MemeberAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(VolonteerTask, VolonteerTaskAdmin)
