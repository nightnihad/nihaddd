# Generated by Django 3.2.4 on 2021-07-24 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_alter_customermodel_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customermodel',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='images/avatar'),
        ),
    ]