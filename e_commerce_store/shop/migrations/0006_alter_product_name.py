# Generated by Django 4.2.2 on 2023-08-12 19:10

from django.db import migrations, models
import e_commerce_store.accounts.validators


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_product_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=10, validators=[e_commerce_store.accounts.validators.letters_only_validator]),
        ),
    ]
