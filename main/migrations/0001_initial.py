# Generated by Django 5.0.8 on 2024-08-07 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('english_certificate', models.BooleanField()),
                ('phone', models.CharField(max_length=13)),
            ],
        ),
    ]
