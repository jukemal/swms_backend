# Generated by Django 3.1.1 on 2020-09-23 12:56

from django.db import migrations, models
import django.db.models.deletion
import month.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reservoirs', '0002_auto_20200817_1115'),
    ]

    operations = [
        migrations.CreateModel(
            name='WaterConsumptionDomestic',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', month.models.MonthField(help_text='Month Value', verbose_name='Month Value')),
                ('water_consumption_domestic', models.IntegerField()),
                ('population', models.IntegerField()),
                ('no_of_families', models.IntegerField()),
                ('no_of_housing_units', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('reservoir', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservoirs.reservoir')),
            ],
            options={
                'ordering': ['reservoir', 'date'],
                'unique_together': {('reservoir', 'date')},
            },
        ),
    ]