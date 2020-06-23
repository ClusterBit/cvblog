from django.contrib import admin
from .models import Customer, Company, Post, PostImages, PostComment, NewsPost, NewsPostImages, NewsPostComment


class PostImagesInline(admin.StackedInline):
    model = PostImages
    extra = 3


class PostCommentsInline(admin.StackedInline):
    model = PostComment


class PostAdmin(admin.ModelAdmin):
    inlines = [PostImagesInline, PostCommentsInline]


class NewsPostImagesInline(admin.StackedInline):
    model = NewsPostImages
    extra = 3


class NewsPostCommentsInline(admin.StackedInline):
    model = NewsPostComment


class NewsPostAdmin(admin.ModelAdmin):
    inlines = [NewsPostCommentsInline, NewsPostImagesInline]


admin.site.register(Customer)
admin.site.register(Company)
admin.site.register(Post, PostAdmin)
admin.site.register(PostImages)
admin.site.register(PostComment)
admin.site.register(NewsPost, NewsPostAdmin)
admin.site.register(NewsPostImages)
admin.site.register(NewsPostComment)

