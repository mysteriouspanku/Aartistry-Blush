# Generated by Django 5.2 on 2025-04-21 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HOME', '0004_posts_caption'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background_gradient', models.CharField(default='linear-gradient(to right, #d16ba5, #86fde8)', max_length=100)),
                ('font_family', models.CharField(default='Arial, sans-serif', max_length=100)),
                ('heading_color', models.CharField(default='#333', max_length=20)),
                ('text_color', models.CharField(default='#555', max_length=20)),
            ],
        ),
    ]
