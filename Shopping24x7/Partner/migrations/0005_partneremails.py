# Generated by Django 3.2.6 on 2021-08-17 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Partner', '0004_partner_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='PartnerEmails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=300)),
            ],
        ),
    ]
