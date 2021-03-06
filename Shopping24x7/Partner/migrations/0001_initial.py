# Generated by Django 2.2.12 on 2021-08-19 06:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Employee', '0001_initial'),
        ('Customer', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PartnerEmails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Payroll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.DateField()),
                ('attendance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Employee.Attendance')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Employee.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=300)),
                ('partner_name', models.CharField(max_length=200)),
                ('locality', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('zipcode', models.IntegerField()),
                ('state', models.CharField(choices=[('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'), ('Andhra Pradesh', 'Andhra Pradesh'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chandigarh', 'Chandigarh'), ('Chattisgarh', 'Chattisgarh'), ('Daman & Diu', 'Daman & Diu'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Maharashtra', 'Maharashtra')], max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(choices=[('India', 'India'), ('USA', 'USA'), ('Japan', 'Japan'), ('UAE', 'UAE'), ('UK', 'UK'), ('Italy', 'Italy'), ('South Africa', 'South Africa')], max_length=200)),
                ('title', models.CharField(choices=[('WORK', 'WORK'), ('HOME', 'HOME')], max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('pincode', models.IntegerField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Customer.Customer')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Employee.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coupon_name', models.CharField(max_length=200)),
                ('coupon_discount', models.FloatField()),
                ('coupon_partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Partner.Partner')),
            ],
        ),
    ]
