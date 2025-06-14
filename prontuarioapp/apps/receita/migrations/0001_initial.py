# Generated by Django 5.2 on 2025-06-04 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Receita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicamento', models.CharField(max_length=255)),
                ('dataEmissao', models.DateField()),
                ('validade', models.DateField()),
            ],
            options={
                'verbose_name': 'Receita',
                'verbose_name_plural': 'Receitas',
                'ordering': ['id'],
            },
        ),
    ]
