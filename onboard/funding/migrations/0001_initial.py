# Generated by Django 4.0.3 on 2022-04-13 06:21

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Funding',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('description', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, default='default.png', null=True, upload_to='')),
                ('people_total', models.IntegerField(blank=True, default=0, null=True)),
                ('target_num', models.IntegerField(blank=True, default=0, null=True)),
                ('curr_num', models.IntegerField(blank=True, default=0, null=True)),
                ('achievement', models.IntegerField(blank=True, default=0, null=True)),
                ('num_limit', models.IntegerField(blank=True, default=0, null=True)),
                ('dday', models.DateField()),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('invest', models.IntegerField(blank=True, default=0, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('funding', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='funding.funding')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
    ]