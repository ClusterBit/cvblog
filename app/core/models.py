from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField
from django_utils.choices import Choices, Choice
from multiselectfield import MultiSelectField
from django.utils.translation import gettext_lazy as _


class CATEGORIES(Choices):
    service = Choice(1, _('Послуги'))
    equipment = Choice(2, _('Обладнання'))
    clothes = Choice(3, _('Одяг'))
    products = Choice(4, _('Продукти'))
    manufacture = Choice(5, _('Виробництво'))
    health = Choice(6, _("Здоров'я"))


class Customer (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=False)
    sur_name = models.CharField(max_length=30, blank=False)
    avatar = ResizedImageField(size=[120, 120], upload_to="customers/avatars/%Y/%m/%d", null=True, blank=True)
    phone = models.CharField(max_length=10, blank=True)


class Company (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=False)
    logo = ResizedImageField(size=[120, 120], upload_to="companies/logos/%Y/%m/%d", null=True, blank=True)
    desc_field = models.TextField(max_length=500, blank=True)
    phone = models.CharField(max_length=10, blank=True)
    location = models.CharField(max_length=30, blank=True)
    category = MultiSelectField(choices=CATEGORIES, default=None)


# each field in this class represents a column in the database table
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    category = models.IntegerField(choices=CATEGORIES, default=None)

    # this class contains metadata and uses the created_on field from the model to sort out data which sorts
    # in descending order by default
    class Meta:
        ordering = ['-created_on']

    # this method is the default human-readable representation of the object. Django will use it in many places
    # such as the admin panel
    def __str__(self):
        return self.title


