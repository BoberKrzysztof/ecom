# Generated by Django 5.0.7 on 2024-08-07 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]