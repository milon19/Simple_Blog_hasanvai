from django.contrib import admin
from .models import Quote, FeaturedPost, Tag, PostImage, Post, Comment

class PostImagesAdmin(admin.StackedInline):
    model = PostImage

class TagsAdmin(admin.StackedInline):
    model = Tag

class PostAdmin(admin.ModelAdmin):
    inlines = [PostImagesAdmin, TagsAdmin]

    class Meta:
        model = Post

admin.site.register(Quote)
admin.site.register(FeaturedPost)
admin.site.register(PostImage)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)