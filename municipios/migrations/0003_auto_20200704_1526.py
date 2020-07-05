# Generated by Django 3.0.7 on 2020-07-04 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('departamentos', '0003_auto_20200704_1357'),
        ('municipios', '0002_auto_20200704_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='municipio',
            name='cod_departamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departamentos.Departamento'),
        ),
    ]
