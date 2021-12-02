# Generated by Django 3.2.7 on 2021-12-02 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projeto', '0003_auto_20211201_2112'),
    ]

    operations = [
        migrations.AddField(
            model_name='projeto',
            name='dataCriacao',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='projeto',
            name='descricao',
            field=models.CharField(default='', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projeto',
            name='foto_projeto',
            field=models.FileField(blank=True, upload_to='media/'),
        ),
        migrations.AddField(
            model_name='projeto',
            name='nome',
            field=models.CharField(default='', max_length=250),
            preserve_default=False,
        ),
    ]
