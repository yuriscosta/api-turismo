# Generated by Django 2.2.4 on 2019-08-06 23:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacoes', '0002_auto_20190806_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliacao',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]