# Generated by Django 2.2.5 on 2020-03-08 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0026_auto_20200308_0746'),
    ]

    operations = [
        migrations.AddField(
            model_name='mobrecharge',
            name='spname',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
