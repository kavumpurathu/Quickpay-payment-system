# Generated by Django 2.2.5 on 2020-03-09 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0029_auto_20200308_1139'),
    ]

    operations = [
        migrations.AddField(
            model_name='recharge',
            name='status',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
