# Generated by Django 3.2.7 on 2021-12-01 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dados_site', '0015_projeto_ferramentas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projeto',
            name='ferramentas',
        ),
        migrations.AddField(
            model_name='ferramenta',
            name='projeto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dados_site.projeto'),
        ),
    ]
