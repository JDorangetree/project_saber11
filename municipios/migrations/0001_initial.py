# Generated by Django 3.0.7 on 2020-07-04 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departamentos', '0003_auto_20200704_1357'),
    ]

    operations = [
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('cod_municipio', models.PositiveIntegerField(unique=True)),
                ('cod_departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departamentos.Departamento')),
            ],
        ),
    ]
