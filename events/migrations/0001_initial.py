# Generated by Django 4.2.1 on 2023-06-04 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Performer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('biog', models.TextField()),
                ('photo', models.FileField(upload_to='')),
                ('weblink', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('stepfree', models.BooleanField(default=False)),
                ('accessible_toilets', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=50)),
                ('published', models.BooleanField(default=False)),
                ('performers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.performer')),
                ('venue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.venue')),
            ],
        ),
    ]