# Generated by Django 3.1.7 on 2021-05-12 18:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0004_auto_20210512_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='scan',
            name='domain_url',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]