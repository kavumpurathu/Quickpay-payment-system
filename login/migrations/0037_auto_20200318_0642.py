# Generated by Django 2.2.5 on 2020-03-18 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0036_complaints_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complaints',
            name='date',
        ),
        migrations.AddField(
            model_name='complaints',
            name='date_com',
            field=models.DateField(default=1),
            preserve_default=False,
        ),
    ]
