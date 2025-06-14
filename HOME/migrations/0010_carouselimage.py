# Generated by Django 5.2 on 2025-06-08 19:49

import HOME.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HOME', '0009_alter_sitesettings_background_gradient_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarouselImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=HOME.models.carousel_upload_path)),
                ('alt_text', models.CharField(blank=True, max_length=255)),
                ('order', models.PositiveIntegerField(default=0, help_text='Order of the image in the carousel')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
    ]
