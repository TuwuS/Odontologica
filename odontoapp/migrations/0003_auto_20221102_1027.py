# Generated by Django 3.2.3 on 2022-11-02 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('odontoapp', '0002_proveedor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='password',
        ),
    ]
