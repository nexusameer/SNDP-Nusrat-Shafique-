# Generated by Django 5.0.7 on 2024-08-19 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.RemoveField(
            model_name='persona',
            name='fb',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='gmail',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='li',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='tw',
        ),
        migrations.AddField(
            model_name='persona',
            name='address',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='persona',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='persona',
            name='facebook_profile',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='persona',
            name='insta_profile',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='persona',
            name='linkedin_profile',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='service_image',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='persona',
            name='phone',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
