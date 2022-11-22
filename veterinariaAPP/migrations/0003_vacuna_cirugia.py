# Generated by Django 4.1.2 on 2022-11-22 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('veterinariaAPP', '0002_estetica'),
    ]

    operations = [
        migrations.CreateModel(
            name='vacuna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.CharField(max_length=100)),
                ('motivo', models.CharField(max_length=100)),
                ('diagnostico', models.CharField(max_length=100)),
                ('tratamiento', models.CharField(max_length=100)),
                ('observaciones', models.CharField(max_length=100)),
                ('valor', models.IntegerField()),
                ('nombre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='veterinariaAPP.mascota')),
            ],
            options={
                'verbose_name': 'vacuna',
                'verbose_name_plural': 'vacunas',
            },
        ),
        migrations.CreateModel(
            name='cirugia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.CharField(max_length=100)),
                ('motivo', models.CharField(max_length=100)),
                ('diagnostico', models.CharField(max_length=100)),
                ('tratamiento', models.CharField(max_length=100)),
                ('observaciones', models.CharField(max_length=100)),
                ('valor', models.IntegerField()),
                ('nombre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='veterinariaAPP.mascota')),
            ],
            options={
                'verbose_name': 'cirugia',
                'verbose_name_plural': 'cirugias',
            },
        ),
    ]
