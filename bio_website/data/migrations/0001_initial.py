# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cell',
            fields=[
                ('FeatureName', models.CharField(serialize=False, primary_key=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='GeneData',
            fields=[
                ('GeneStandardName', models.CharField(max_length=10)),
                ('SystematicID', models.CharField(serialize=False, primary_key=True, max_length=50)),
                ('Synonyms', models.CharField(max_length=50)),
                ('Product', models.CharField(max_length=200)),
                ('ProductSize', models.CharField(max_length=50)),
                ('Pic_1', models.ImageField(upload_to='')),
                ('Pic_2', models.ImageField(upload_to='')),
                ('Pic_3', models.ImageField(upload_to='')),
                ('Pic_4', models.ImageField(upload_to='')),
                ('Pic_1text', models.CharField(default='Pic_1', max_length=50)),
                ('Pic_2text', models.CharField(default='Pic_2', max_length=50)),
                ('Pic_3text', models.CharField(default='Pic_3', max_length=50)),
                ('Pic_4text', models.CharField(default='Pic_4', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Microtubule',
            fields=[
                ('FeatureName', models.CharField(serialize=False, primary_key=True, max_length=50)),
                ('SystematicIDs', models.ManyToManyField(to='data.GeneData')),
            ],
        ),
        migrations.CreateModel(
            name='Mitochondria',
            fields=[
                ('FeatureName', models.CharField(serialize=False, primary_key=True, max_length=50)),
                ('SystematicIDs', models.ManyToManyField(to='data.GeneData')),
            ],
        ),
        migrations.AddField(
            model_name='cell',
            name='SystematicIDs',
            field=models.ManyToManyField(to='data.GeneData'),
        ),
    ]
