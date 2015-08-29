from django.contrib import admin

from .models import MemeberGroup, Memeber


class MemeberGroupAdmin(admin.ModelAdmin):
    model = MemeberGroup
    list_display = ('name', )


class MemeberAdmin(admin.ModelAdmin):
    model = Memeber
    list_display = ('full_name', )


admin.site.register(MemeberGroup, MemeberGroupAdmin)
admin.site.register(Memeber, MemeberAdmin)
