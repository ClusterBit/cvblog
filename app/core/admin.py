from django.contrib import admin
from .models import Customer, Company, Post, PostImages, PostComment


class PhotoInline(admin.StackedInline):
    model = PostImages
    extra = 3


class CommentsInline(admin.StackedInline):
    model = PostComment


class PostAdmin(admin.ModelAdmin):
    inlines = [PhotoInline, CommentsInline]


admin.site.register(Customer)
admin.site.register(Company)
admin.site.register(Post, PostAdmin)
admin.site.register(PostImages)
admin.site.register(PostComment)

