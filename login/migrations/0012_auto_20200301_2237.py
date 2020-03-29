# Generated by Django 2.2.5 on 2020-03-02 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0011_auto_20200301_2224'),
    ]

    operations = [
        migrations.RenameField(
            model_name='complaints',
            old_name='uname',
            new_name='name',
        ),
        migrations.AddField(
            model_name='complaints',
            name='username',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
