# Generated by Django 3.2.7 on 2021-12-02 00:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projeto', '0006_alter_projeto_foto_projeto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projeto',
            name='foto_projeto',
        ),
    ]
