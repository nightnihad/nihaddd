# Generated by Django 3.2.4 on 2021-06-30 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customermodel',
            options={'verbose_name': 'Istifadeçi', 'verbose_name_plural': 'İstifadəçilər'},
        ),
        migrations.AlterModelTable(
            name='customermodel',
            table='İstifadəçilər',
        ),
    ]