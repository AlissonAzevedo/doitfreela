# Generated by Django 3.2.7 on 2021-12-01 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dados_site', '0006_projeto_ferramentas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projeto',
            name='ferramentas',
        ),
    ]
