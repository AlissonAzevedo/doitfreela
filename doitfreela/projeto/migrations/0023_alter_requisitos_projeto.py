# Generated by Django 3.2.7 on 2021-12-06 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projeto', '0022_alter_requisitos_projeto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requisitos',
            name='projeto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projeto.projeto'),
        ),
    ]
