# Generated by Django 2.2.6 on 2020-08-12 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_auto_20200812_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='cpf',
            field=models.CharField(max_length=11, unique=True),
        ),
    ]
