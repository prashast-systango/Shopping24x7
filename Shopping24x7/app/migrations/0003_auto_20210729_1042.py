# Generated by Django 2.2.12 on 2021-07-29 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210729_0826'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='quntity',
            new_name='quantity',
        ),
        migrations.RemoveField(
            model_name='location',
            name='type',
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('M', 'Mobile'), ('L', 'Laptop'), ('AC', 'Accessories')], max_length=2),
        ),
    ]