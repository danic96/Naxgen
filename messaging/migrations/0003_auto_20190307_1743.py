# Generated by Django 2.1.7 on 2019-03-07 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0002_auto_20190307_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(default=1, to='messaging.Group'),
        ),
    ]
