# Generated by Django 4.1.6 on 2023-02-09 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='category/'),
        ),
        migrations.AddField(
            model_name='category',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
