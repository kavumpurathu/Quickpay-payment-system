# Generated by Django 2.2.5 on 2020-02-25 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20200223_2231'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('mob', models.IntegerField()),
                ('email', models.CharField(max_length=100)),
            ],
        ),
    ]
