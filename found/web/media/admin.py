from django.contrib import admin

from .models import PhotoGroup, Photo, VideoGroup, Video

class PhotoGroupAdmin(admin.ModelAdmin):
    list_display = ('title', )


class PhotoAdmin(admin.ModelAdmin):
    pass


class VideoGroupAdmin(admin.ModelAdmin):
    pass


class VideoAdmin(admin.ModelAdmin):
    pass

admin.site.register(PhotoGroup, PhotoGroupAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(VideoGroup, VideoGroupAdmin)
admin.site.register(Video, VideoAdmin)
