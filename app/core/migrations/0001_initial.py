# Generated by Django 2.0.1 on 2020-06-17 13:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms
import django_utils.choices
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('logo', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='JPEG', keep_meta=True, null=True, quality=75, size=[120, 120], upload_to='companies/logos/%Y/%m/%d')),
                ('desc_field', models.TextField(blank=True, max_length=500)),
                ('phone', models.CharField(blank=True, max_length=10)),
                ('location', models.CharField(blank=True, max_length=30)),
                ('category', multiselectfield.db.fields.MultiSelectField(choices=[(1, django_utils.choices.Choice(1, 'Послуги')), (2, django_utils.choices.Choice(2, 'Обладнання')), (3, django_utils.choices.Choice(3, 'Одяг')), (4, django_utils.choices.Choice(4, 'Продукти')), (5, django_utils.choices.Choice(5, 'Виробництво')), (6, django_utils.choices.Choice(6, "Здоров'я"))], default=None, max_length=11)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('sur_name', models.CharField(max_length=150)),
                ('avatar', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='JPEG', keep_meta=True, null=True, quality=75, size=[120, 120], upload_to='customers/avatars/%Y/%m/%d')),
                ('phone', models.CharField(blank=True, max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('content', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('category', multiselectfield.db.fields.MultiSelectField(choices=[(1, django_utils.choices.Choice(1, 'Послуги')), (2, django_utils.choices.Choice(2, 'Обладнання')), (3, django_utils.choices.Choice(3, 'Одяг')), (4, django_utils.choices.Choice(4, 'Продукти')), (5, django_utils.choices.Choice(5, 'Виробництво')), (6, django_utils.choices.Choice(6, "Здоров'я"))], default=None, max_length=11)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Company')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
