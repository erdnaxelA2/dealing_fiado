# Generated by Django 3.2.3 on 2021-07-01 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dealing_fiado', '0002_auto_20210629_2330'),
    ]

    operations = [
        migrations.AddField(
            model_name='venda',
            name='mercadorias',
            field=models.ManyToManyField(blank=True, to='dealing_fiado.Produto'),
        ),
    ]
