# Generated by Django 3.0.2 on 2020-02-07 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostelName', models.CharField(max_length=120)),
                ('email', models.CharField(max_length=120)),
                ('location', models.CharField(max_length=120)),
            ],
        ),
    ]