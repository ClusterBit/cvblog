from django.contrib import admin
from .models import Customer, Company, Post, PostImages


class PhotoInline(admin.StackedInline):
    model = PostImages
    extra = 3


class PostAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]


admin.site.register(Customer)
admin.site.register(Company)
admin.site.register(Post, PostAdmin)
admin.site.register(PostImages)

