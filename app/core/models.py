from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django_resized import ResizedImageField
from django_utils.choices import Choices, Choice
from multiselectfield import MultiSelectField
from django.utils.translation import gettext_lazy as _
from autoslug import AutoSlugField


class CATEGORIES(Choices):
    service = Choice(1, _('Послуги'))
    equipment = Choice(2, _('Дозвілля'))
    clothes = Choice(3, _('Одяг'))
    products = Choice(4, _('Продукти'))
    manufacture = Choice(5, _('Виробництво'))
    health = Choice(6, _("Здоров'я"))


class Customer (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=False)
    sur_name = models.CharField(max_length=150, blank=False)
    avatar = ResizedImageField(size=[150, 150], upload_to="customers/avatars/%Y/%m/%d", null=True, blank=True)
    phone = models.CharField(max_length=10, blank=True)


class Company (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=False)
    logo = ResizedImageField(size=[150, 150], upload_to="companies/logos/%Y/%m/%d", null=True, blank=True)
    short_content = models.TextField(max_length=200, blank=True)
    content = models.TextField(max_length=1000, blank=True)
    phone = models.CharField(max_length=10, blank=True)
    location = models.CharField(max_length=100, blank=True)
    website_link = models.CharField(max_length=100, blank=True)
    category = MultiSelectField(choices=CATEGORIES, default=None)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = AutoSlugField(populate_from='title', always_update=True, unique=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    category = MultiSelectField(choices=CATEGORIES, default=None)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})


class PostImages(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = ResizedImageField(size=[1000, 1000], upload_to="posts/pictures/%Y/%m/%d", null=True, blank=True)


class PostComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=300, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)


class NewsPost(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = AutoSlugField(populate_from='title', always_update=True, unique=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    category = MultiSelectField(choices=CATEGORIES, default=None)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news_detail', kwargs={'slug': self.slug})


class NewsPostImages(models.Model):
    post = models.ForeignKey(NewsPost, on_delete=models.CASCADE)
    image = ResizedImageField(size=[1000, 1000], upload_to="news/pictures/%Y/%m/%d", null=True, blank=True)


class NewsPostComment(models.Model):
    post = models.ForeignKey(NewsPost, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=300, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)


class ExportPost(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = AutoSlugField(populate_from='title', always_update=True, unique=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    category = MultiSelectField(choices=CATEGORIES, default=None)
    website_link = models.CharField(max_length=100, blank=True)
