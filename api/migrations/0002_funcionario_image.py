# Generated by Django 2.2.9 on 2022-02-21 19:20

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=api.models.upload_image_funcionario),
        ),
    ]