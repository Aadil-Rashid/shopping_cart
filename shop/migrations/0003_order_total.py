# Generated by Django 3.0.8 on 2020-09-03 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.IntegerField(default='1'),
            preserve_default=False,
        ),
    ]
