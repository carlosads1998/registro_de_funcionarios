# Generated by Django 2.2.9 on 2022-02-22 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_funcionario_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='sexo',
            field=models.CharField(choices=[('F', 'Feminino'), ('M', 'Masculino'), ('N', 'Prefiro não informar')], default=1, max_length=20),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='status',
            field=models.CharField(choices=[('ativo', 'empregado'), ('desativado', 'demitido')], default=1, max_length=20),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='identificador',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='usuario',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]