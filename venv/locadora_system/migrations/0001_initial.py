# Generated by Django 4.1.6 on 2023-02-12 23:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=100)),
                ('dt_criacao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Aluguel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filme', models.CharField(max_length=200)),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('descricao', models.CharField(max_length=200)),
                ('ano_lancamento', models.DecimalField(decimal_places=0, max_digits=4)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=7)),
                ('observacoes', models.TextField(blank=True, null=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locadora_system.categoria')),
            ],
            options={
                'verbose_name_plural': 'Alugueis',
            },
        ),
    ]
