# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-18 02:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.CharField(max_length=20, verbose_name='Latitud')),
                ('longitude', models.CharField(max_length=20, verbose_name='Longitud')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Perfil de Usuario',
                'verbose_name_plural': 'Perfiles de Usuario',
            },
        ),
        migrations.AlterModelOptions(
            name='choice',
            options={'verbose_name': 'Opción', 'verbose_name_plural': 'Opciones'},
        ),
        migrations.AlterModelOptions(
            name='recommendation',
            options={'verbose_name': 'Recomendación', 'verbose_name_plural': 'Recomendaciones'},
        ),
        migrations.RemoveField(
            model_name='answer',
            name='question',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='recommendations',
        ),
        migrations.AddField(
            model_name='recommendation',
            name='choice',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.Choice', verbose_name='Opción'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='choice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Choice', verbose_name='Opción'),
        ),
        migrations.AlterField(
            model_name='recommendation',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Category', verbose_name='Categoría'),
        ),
    ]
