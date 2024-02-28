from django.contrib import admin
from .models import *

admin.site.register(Course)
admin.site.register(Video)
admin.site.register(LikedVideo)
admin.site.register(WatchLaterVideo)


