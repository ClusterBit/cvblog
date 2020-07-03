from django.contrib import admin
from .models import Customer, Company, Post, PostImages, PostComment, NewsPost, NewsPostImages, NewsPostComment, \
    ExportPost
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms


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


class NewsPostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = NewsPost
        fields = '__all__'


class NewsPostAdmin(admin.ModelAdmin):
    form = NewsPostAdminForm
    inlines = [NewsPostCommentsInline, NewsPostImagesInline]


admin.site.register(Customer)
admin.site.register(Company)
admin.site.register(Post, PostAdmin)
admin.site.register(PostImages)
admin.site.register(PostComment)
admin.site.register(NewsPost, NewsPostAdmin)
admin.site.register(NewsPostImages)
admin.site.register(NewsPostComment)
admin.site.register(ExportPost)
