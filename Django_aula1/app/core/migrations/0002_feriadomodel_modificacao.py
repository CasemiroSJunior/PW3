# Generated by Django 5.1.7 on 2025-04-03 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feriadomodel',
            name='modificacao',
            field=models.DateTimeField(auto_now=True, verbose_name='Modificado em'),
        ),
    ]
