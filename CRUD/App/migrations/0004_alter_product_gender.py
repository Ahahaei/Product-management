# Generated by Django 4.2.1 on 2023-06-03 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_rename_created_at_product_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='gender',
            field=models.CharField(choices=[('M', 'M'), ('F', 'F')], max_length=1, null=True),
        ),
    ]
