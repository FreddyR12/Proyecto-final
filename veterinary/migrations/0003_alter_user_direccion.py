# Generated by Django 4.1.3 on 2022-11-04 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veterinary', '0002_veterinary_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='direccion',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
