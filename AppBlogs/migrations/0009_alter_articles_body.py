# Generated by Django 4.2.6 on 2023-11-23 16:06

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlogs', '0008_alter_articles_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='body',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
