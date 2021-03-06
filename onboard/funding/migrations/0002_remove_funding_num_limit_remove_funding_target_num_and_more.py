# Generated by Django 4.0.3 on 2022-04-13 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funding', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='funding',
            name='num_limit',
        ),
        migrations.RemoveField(
            model_name='funding',
            name='target_num',
        ),
        migrations.AddField(
            model_name='funding',
            name='limitation',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='funding',
            name='target',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='funding',
            name='title',
            field=models.CharField(default='', max_length=200),
        ),
    ]
