# Generated by Django 4.2.5 on 2023-10-05 01:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0008_rename_images1_articles_image1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='image1',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='image2',
        ),
    ]
