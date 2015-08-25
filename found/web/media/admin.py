from django.contrib import admin

from .models import Galery, Photo

class GaleryAdmin(admin.ModelAdmin):
    model = Galery
    list_display = ('title', )


class PhotoAdmin(admin.ModelAdmin):
    model = Photo


admin.site.register(Galery, GaleryAdmin)
admin.site.register(Photo, PhotoAdmin)
