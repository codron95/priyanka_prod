from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(post)
admin.site.register(photo)
admin.site.register(comment)
admin.site.register(subscribers)
admin.site.register(comment_photo)

