# Generated by Django 3.1.1 on 2020-09-13 08:12

from django.db import migrations
import month.models


class Migration(migrations.Migration):

    dependencies = [
        ('water_level', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='waterlevel',
            options={'ordering': ['reservoir', 'date']},
        ),
        migrations.AlterField(
            model_name='waterlevel',
            name='date',
            field=month.models.MonthField(help_text='Month Value', verbose_name='Month Value'),
        ),
    ]
