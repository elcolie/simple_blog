from django.contrib import admin

from .models import Post

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "updated", "timestamp"] # title use lowercase
    list_display_links = ["updated"]
    list_filter = ["updated", "timestamp"]
    class Meta:
        model = Post

admin.site.register(Post, PostModelAdmin)
