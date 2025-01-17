# Generated by Django 4.2.4 on 2023-09-29 00:43

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('quickintro', models.TextField()),
                ('intro', models.TextField()),
                ('image1', models.ImageField(null=True, upload_to='images')),
                ('body1', models.TextField(null=True)),
                ('image2', models.ImageField(null=True, upload_to='images')),
                ('body2', models.TextField(null=True)),
                ('image3', models.ImageField(null=True, upload_to='images')),
                ('body3', models.TextField(null=True)),
                ('conc', models.TextField()),
                ('date_posted', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Usercomments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date_posted', models.DateField(default=django.utils.timezone.now)),
                ('comnt', models.TextField()),
                ('relatedarticle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webpages.articles')),
            ],
        ),
    ]
