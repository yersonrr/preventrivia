# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='Fecha y hora')),
            ],
            options={
                'verbose_name': 'Respuesta',
                'verbose_name_plural': 'Respuestas',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=200, verbose_name='Texto')),
                ('value', models.IntegerField(verbose_name='Valor')),
            ],
            options={
                'verbose_name': 'Opcion',
                'verbose_name_plural': 'Opciones',
            },
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Encuesta',
                'verbose_name_plural': 'Encuestas',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=300, verbose_name='Texto')),
                ('category', models.ForeignKey(verbose_name='Categoria', to='polls.Category')),
                ('poll', models.ForeignKey(verbose_name='Encuesta', to='polls.Poll')),
            ],
            options={
                'verbose_name': 'Pregunta',
                'verbose_name_plural': 'Preguntas',
            },
        ),
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(verbose_name='Texto')),
                ('category', models.ForeignKey(verbose_name='Categoria', to='polls.Category')),
            ],
            options={
                'verbose_name': 'Recomendacion',
                'verbose_name_plural': 'Recomendaciones',
            },
        ),
        migrations.CreateModel(
            name='Tip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(verbose_name='Texto')),
            ],
            options={
                'verbose_name': 'Tip',
                'verbose_name_plural': 'Tips',
            },
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(verbose_name='Pregunta', to='polls.Question'),
        ),
        migrations.AddField(
            model_name='choice',
            name='recommendations',
            field=models.ManyToManyField(to='polls.Recommendation', verbose_name='Recomendaciones', blank=True),
        ),
        migrations.AddField(
            model_name='answer',
            name='choice',
            field=models.ForeignKey(verbose_name='Opcion', to='polls.Choice'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(verbose_name='Pregunta', to='polls.Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(verbose_name='Usuario', to=settings.AUTH_USER_MODEL),
        ),
    ]
