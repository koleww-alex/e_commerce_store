# Generated by Django 4.2.2 on 2023-08-12 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_alter_fruitstoreuser_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fruitstoreuser',
            name='phone_number',
            field=models.CharField(blank=True, null=True),
        ),
    ]
