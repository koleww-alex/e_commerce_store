# Generated by Django 4.2.2 on 2023-08-09 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_fruitstoreuser_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fruitstoreuser',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Do not show', 'Do not show')], max_length=11, null=True),
        ),
    ]
