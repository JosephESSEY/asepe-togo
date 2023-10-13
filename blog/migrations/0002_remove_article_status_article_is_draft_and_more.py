# Generated by Django 4.1 on 2022-10-11 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='status',
        ),
        migrations.AddField(
            model_name='article',
            name='is_draft',
            field=models.BooleanField(default=True),
        ),
        migrations.DeleteModel(
            name='Brouillon',
        ),
    ]
