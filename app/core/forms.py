from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Customer, Company, Post, PostImages, PostComment


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
        fields = ('name', 'logo', 'desc_field', 'phone', 'location', 'category')


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'category')

        def __init__(self, *args, **kwargs):
            self.user = kwargs.pop('user', None)
            super(PostCreateForm, self).__init__(*args, **kwargs)

        def save(self, commit=True):
            obj = super(PostCreateForm, self).save(commit=False)
            obj.user = self.user
            if commit:
                obj.save()
            return obj


class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')

    class Meta:
        model = PostImages
        fields = ('image',)


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = ('content',)

        def __init__(self, *args, **kwargs):
            self.user = kwargs.pop('user', None)
            super(CommentCreateForm, self).__init__(*args, **kwargs)

        def save(self, commit=True):
            obj = super(CommentCreateForm, self).save(commit=False)
            obj.user = self.user
            if commit:
                obj.save()
            return obj
