# Generated by Django 3.0.4 on 2020-04-15 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vislib', '0003_auto_20200415_0913'),
    ]

    operations = [
        migrations.AddField(
            model_name='sourcedatabase',
            name='is_private',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='sourcedatabase',
            name='status',
            field=models.IntegerField(default=1),
        ),
    ]
