# Generated by Django 4.0.2 on 2022-02-03 23:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hour', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Athlete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=15)),
                ('plan', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='athlete_plan', to='athletes.plan')),
                ('schedule', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='athlete_schedule', to='athletes.schedule')),
            ],
        ),
    ]
