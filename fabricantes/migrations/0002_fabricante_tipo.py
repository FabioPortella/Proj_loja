# Generated by Django 4.2.1 on 2023-06-20 00:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tipo', '0001_initial'),
        ('fabricantes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fabricante',
            name='tipo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tipo.tipos'),
        ),
    ]
