# Generated by Django 3.2.7 on 2021-12-01 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dados_site', '0013_auto_20211201_1407'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projeto',
            name='ferramentas',
        ),
    ]