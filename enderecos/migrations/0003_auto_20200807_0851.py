# Generated by Django 2.2.6 on 2020-08-07 11:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enderecos', '0002_auto_20200807_0834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endereco',
            name='user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='enderecos', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]