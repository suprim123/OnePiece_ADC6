# Generated by Django 3.0.1 on 2020-01-29 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hostel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=25)),
                ('Price', models.CharField(max_length=7)),
                ('Description', models.TextField()),
                ('Location', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Location', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Location', models.CharField(max_length=30)),
                ('Hostels', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hostel.Hostel')),
            ],
        ),
        migrations.CreateModel(
            name='HostelDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.CharField(max_length=20)),
                ('Price', models.IntegerField(default=0)),
                ('Hostel', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Hostel.Hostel')),
            ],
        ),
        migrations.AddField(
            model_name='hostel',
            name='addresses',
            field=models.ManyToManyField(to='Hostel.Location'),
        ),
    ]
