# Generated by Django 2.0.1 on 2020-06-23 12:01

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms
import django_utils.choices
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0007_auto_20200623_1106'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', autoslug.fields.AutoSlugField(always_update=True, editable=False, null=True, populate_from='title', unique=True)),
                ('content', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('category', multiselectfield.db.fields.MultiSelectField(choices=[(1, django_utils.choices.Choice(1, 'Послуги')), (2, django_utils.choices.Choice(2, 'Дозвілля')), (3, django_utils.choices.Choice(3, 'Одяг')), (4, django_utils.choices.Choice(4, 'Продукти')), (5, django_utils.choices.Choice(5, 'Виробництво')), (6, django_utils.choices.Choice(6, "Здоров'я"))], default=None, max_length=11)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='NewsPostComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=300)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.NewsPost')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='NewsPostImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='PNG', keep_meta=True, null=True, quality=100, size=[1000, 1000], upload_to='news/pictures/%Y/%m/%d')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.NewsPost')),
            ],
        ),
    ]