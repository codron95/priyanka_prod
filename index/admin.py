from django.contrib import admin
from .models import *
from index.helpers import generate_link
# Register your models here.

class PostAdmin(admin.ModelAdmin):

    list_display = ("head", "created_date")

    def save_model(self, request, post_instance, form, change):
        post_instance.link = generate_link(post_instance.head)
        super().save_model(request, post_instance, form, change)


admin.site.register(post, PostAdmin)
admin.site.register(photo)
admin.site.register(comment)
admin.site.register(subscribers)
admin.site.register(comment_photo)