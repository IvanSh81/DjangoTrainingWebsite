# Generated by Django 4.1.2 on 2022-10-06 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pricetable',
            options={'verbose_name': 'Услугу', 'verbose_name_plural': 'Услуги'},
        ),
    ]
