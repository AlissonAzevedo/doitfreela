# Generated by Django 3.2.8 on 2021-10-29 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dados_site', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ferramenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250)),
                ('foto_ferramenta', models.FileField(null=True, upload_to='media/')),
            ],
        ),
    ]