# Generated by Django 2.2.5 on 2020-02-24 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_auto_20191123_0448'),
    ]

    operations = [
        migrations.CreateModel(
            name='serviceprovider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('website', models.CharField(max_length=100)),
                ('mob', models.IntegerField()),
                ('email', models.CharField(max_length=100)),
            ],
        ),
    ]
