# Generated by Django 5.1.2 on 2024-12-13 04:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Member',
            new_name='Members',
        ),
    ]