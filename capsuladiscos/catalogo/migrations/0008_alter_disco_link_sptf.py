# Generated by Django 4.0.1 on 2022-06-13 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0007_remove_disco_link_tienda_disco_link_tienda_cas_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disco',
            name='link_sptf',
            field=models.CharField(max_length=250, null=True, verbose_name='Disco inserto desde Spotify'),
        ),
    ]
