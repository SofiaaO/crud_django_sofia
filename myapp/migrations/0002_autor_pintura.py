# Generated by Django 5.0.7 on 2024-07-20 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='autor',
            name='Pintura',
            field=models.CharField(default='Óleo', max_length=50, verbose_name='Estilo de pintura'),
        ),
    ]
