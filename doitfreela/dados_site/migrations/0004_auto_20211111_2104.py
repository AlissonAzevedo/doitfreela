# Generated by Django 3.2.7 on 2021-11-12 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dados_site', '0003_ferramenta_descricao'),
    ]

    operations = [
        migrations.CreateModel(
            name='Requisitos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250, null=True)),
                ('descricao', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='ferramenta',
            name='descricao',
            field=models.CharField(max_length=250),
        ),
    ]
