# Generated by Django 2.2.9 on 2022-02-22 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20220221_2252'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='funcionario',
            name='sexo',
        ),
        migrations.RemoveField(
            model_name='funcionario',
            name='status',
        ),
    ]