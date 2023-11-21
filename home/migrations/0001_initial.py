# Generated by Django 4.2.7 on 2023-11-18 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('account', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=40)),
                ('lc_number', models.CharField(max_length=40)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
