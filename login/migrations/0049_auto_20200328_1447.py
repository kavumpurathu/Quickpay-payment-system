# Generated by Django 2.2.5 on 2020-03-28 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0048_complaints_sta'),
    ]

    operations = [
        migrations.RenameField(
            model_name='complaints',
            old_name='sta',
            new_name='status',
        ),
    ]
