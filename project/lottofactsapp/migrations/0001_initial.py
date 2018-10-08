# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-08 14:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Draw',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('draw_number', models.DecimalField(decimal_places=0, max_digits=12)),
                ('draw_result', models.TextField()),
                ('message', models.TextField()),
                ('top_prize', models.DecimalField(decimal_places=0, max_digits=12)),
            ],
        ),
        migrations.CreateModel(
            name='Lotto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lotto_name', models.CharField(max_length=200)),
                ('lotto_country', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Prizes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('winners', models.DecimalField(decimal_places=0, max_digits=9)),
                ('match', models.TextField()),
                ('prize_type', models.TextField()),
                ('prize', models.DecimalField(decimal_places=0, max_digits=12)),
                ('draw', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lottofactsapp.Draw')),
                ('lotto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lottofactsapp.Lotto')),
            ],
        ),
        migrations.AddField(
            model_name='draw',
            name='lotto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lottofactsapp.Lotto'),
        ),
    ]