# Generated by Django 4.2.3 on 2023-07-29 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='timesstamp',
            new_name='timestamp',
        ),
    ]
