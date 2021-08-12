# Generated by Django 3.2.5 on 2021-08-05 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0001_initial'),
        ('Customer', '0001_initial'),
        ('Partner', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='coupon',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='product',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='user',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='Cart',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='product',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
        migrations.RemoveField(
            model_name='orderplaced',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='orderplaced',
            name='product',
        ),
        migrations.RemoveField(
            model_name='orderplaced',
            name='user',
        ),
        migrations.AlterField(
            model_name='location',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Customer.customer'),
        ),
        migrations.AlterField(
            model_name='location',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Employee.employee'),
        ),
        migrations.AlterField(
            model_name='payroll',
            name='attendance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Employee.attendance'),
        ),
        migrations.AlterField(
            model_name='payroll',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Employee.employee'),
        ),
        migrations.DeleteModel(
            name='Attendance',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
        migrations.DeleteModel(
            name='OrderPlaced',
        ),
    ]
