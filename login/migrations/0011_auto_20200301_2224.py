# Generated by Django 2.2.5 on 2020-03-02 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0010_serviceprovider_uname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complaints',
            name='refno',
        ),
        migrations.AddField(
            model_name='complaints',
            name='replay',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='complaints',
            name='uname',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
