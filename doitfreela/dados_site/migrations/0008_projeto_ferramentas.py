# Generated by Django 3.2.7 on 2021-12-01 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dados_site', '0007_remove_projeto_ferramentas'),
    ]

    operations = [
        migrations.AddField(
            model_name='projeto',
            name='ferramentas',
            field=models.ManyToManyField(to='dados_site.Ferramenta'),
        ),
    ]
