# Generated by Django 2.2 on 2020-02-11 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Colores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=500)),
                ('sigla', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Marcas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=500)),
                ('sigla', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Modelos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=500)),
                ('sigla', models.CharField(max_length=100)),
                ('marcas_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.Marcas')),
            ],
        ),
        migrations.CreateModel(
            name='Autos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.IntegerField()),
                ('descripcion', models.CharField(max_length=1024)),
                ('colores', models.ManyToManyField(to='crud.Colores')),
                ('modelo_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.Modelos')),
            ],
        ),
    ]