# Generated by Django 5.2 on 2025-06-04 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=11, unique=True, verbose_name='CPF')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('dataNascimento', models.DateField(max_length=100, verbose_name='Data de Nascimento')),
            ],
            options={
                'verbose_name': 'Paciente',
                'verbose_name_plural': 'Paciente',
                'ordering': ['id'],
            },
        ),
    ]
