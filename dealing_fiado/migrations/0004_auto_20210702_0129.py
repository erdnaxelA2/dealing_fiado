# Generated by Django 3.2.3 on 2021-07-02 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dealing_fiado', '0003_venda_mercadorias'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empregado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ponto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entrada', models.DateTimeField(blank=True)),
                ('intervalo', models.DateTimeField(blank=True)),
                ('retorno', models.DateTimeField(blank=True)),
                ('saida', models.DateTimeField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Folha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicial', models.DateTimeField()),
                ('data_final', models.DateTimeField(blank=True)),
                ('empregado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dealing_fiado.empregado')),
                ('pontos', models.ManyToManyField(blank=True, to='dealing_fiado.Ponto')),
            ],
        ),
        migrations.AddField(
            model_name='empregado',
            name='folhas',
            field=models.ManyToManyField(blank=True, related_name='empregado_folhas', to='dealing_fiado.Folha'),
        ),
    ]
