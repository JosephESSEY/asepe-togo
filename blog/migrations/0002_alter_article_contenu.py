# Generated by Django 4.2.6 on 2023-10-06 13:03

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='contenu',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
