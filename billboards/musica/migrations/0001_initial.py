# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cancion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nomcancion', models.TextField()),
                ('autor', models.TextField()),
                ('album', models.TextField()),
                ('duracion', models.IntegerField()),
                ('popularidad', models.IntegerField()),
                ('uri', models.TextField()),
                ('spotify', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Lista',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('puesto', models.IntegerField()),
                ('semana', models.IntegerField()),
                ('cancion', models.ForeignKey(to='musica.Cancion')),
            ],
            options={
                'ordering': ['-puesto'],
            },
        ),
    ]
