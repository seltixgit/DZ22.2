# Generated by Django 4.2.2 on 2024-08-14 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_version_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='version',
            old_name='owner',
            new_name='author',
        ),
    ]
