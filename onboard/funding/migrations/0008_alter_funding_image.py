# Generated by Django 4.0.3 on 2022-04-14 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funding', '0007_remove_funding_achievement_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funding',
            name='image',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to=''),
        ),
    ]