# Generated by Django 4.2.6 on 2023-11-21 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlogs', '0005_alter_articles_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='image',
            field=models.ImageField(null=True, upload_to='blogImages'),
        ),
    ]
