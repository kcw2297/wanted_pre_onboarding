# Generated by Django 4.0.3 on 2022-04-13 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funding', '0002_remove_funding_num_limit_remove_funding_target_num_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funding',
            name='title',
            field=models.CharField(default='default title', max_length=200),
        ),
    ]