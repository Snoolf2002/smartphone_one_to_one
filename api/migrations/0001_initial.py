# Generated by Django 4.1.7 on 2023-03-15 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=255)),
                ('ram', models.IntegerField()),
                ('memory', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Smartphones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('model', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('img_url', models.CharField(default='no image', max_length=255)),
                ('details', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.details')),
            ],
        ),
    ]
