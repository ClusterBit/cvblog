from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from pytils.translit import slugify

from .models import Customer, Company, Post, PostImages, PostComment, NewsPost, NewsPostImages, NewsPostComment


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email', error_messages={'exists': 'This already exists!'})

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError(self.fields['email'].error_messages['exists'])
        return self.cleaned_data['email']


class CustomerSignForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('name', 'sur_name', 'avatar', 'phone')


class CompanySignForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('name', 'logo', 'short_content', 'content', 'phone', 'website_link', 'location', 'category')


# --------------------------------------------------------POST
class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'category')

        def __init__(self, *args, **kwargs):
            self.user = kwargs.pop('user', None)
            super(PostCreateForm, self).__init__(*args, **kwargs)

        def save(self, commit=True):
            obj = super(PostCreateForm, self).save(commit=False)
            obj.slug = self.slug or slugify(self.title)
            obj.user = self.user
            if commit:
                obj.save()
            return obj


class ImagePostForm(forms.ModelForm):
    image = forms.ImageField(label='Image')

    class Meta:
        model = PostImages
        fields = ('image',)


class CommentCreatePostForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = ('content',)

        def __init__(self, *args, **kwargs):
            self.user = kwargs.pop('user', None)
            super(CommentCreatePostForm, self).__init__(*args, **kwargs)

        def save(self, commit=True):
            obj = super(CommentCreatePostForm, self).save(commit=False)
            obj.user = self.user
            if commit:
                obj.save()
            return obj


# --------------------------------------------------------NEWS
class NewsPostCreateForm(forms.ModelForm):
    class Meta:
        model = NewsPost
        fields = ('title', 'content', 'category')

        def __init__(self, *args, **kwargs):
            self.user = kwargs.pop('user', None)
            super(NewsPostCreateForm, self).__init__(*args, **kwargs)

        def save(self, commit=True):
            obj = super(NewsPostCreateForm, self).save(commit=False)
            obj.slug = self.slug or slugify(self.title)
            obj.user = self.user
            if commit:
                obj.save()
            return obj


class ImageNewsPostForm(forms.ModelForm):
    image = forms.ImageField(label='Image')

    class Meta:
        model = NewsPostImages
        fields = ('image',)


class CommentCreateNewsPostForm(forms.ModelForm):
    class Meta:
        model = NewsPostComment
        fields = ('content',)

        def __init__(self, *args, **kwargs):
            self.user = kwargs.pop('user', None)
            super(CommentCreateNewsPostForm, self).__init__(*args, **kwargs)

        def save(self, commit=True):
            obj = super(CommentCreateNewsPostForm, self).save(commit=False)
            obj.user = self.user
            if commit:
                obj.save()
            return obj
