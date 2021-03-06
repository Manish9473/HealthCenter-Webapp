# Generated by Django 2.1.5 on 2019-02-21 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('company', models.CharField(max_length=150)),
                ('expiryDate', models.DateTimeField(auto_now_add=True)),
                ('manufacturedDate', models.DateTimeField(auto_now_add=True)),
                ('quantity', models.PositiveIntegerField()),
            ],
        ),
    ]
