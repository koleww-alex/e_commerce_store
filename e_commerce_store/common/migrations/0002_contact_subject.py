# Generated by Django 4.2.2 on 2023-08-12 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='subject',
            field=models.CharField(default='null', max_length=20),
            preserve_default=False,
        ),
    ]
