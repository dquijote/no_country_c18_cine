# Generated by Django 3.2 on 2024-06-09 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_alter_movies_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movies',
            options={'verbose_name': 'Movie', 'verbose_name_plural': 'Movies'},
        ),
        migrations.CreateModel(
            name='Showtimes',
            fields=[
                ('st_id', models.AutoField(primary_key=True, serialize=False)),
                ('price', models.IntegerField()),
                ('date', models.DateField(max_length=10)),
                ('time', models.TimeField(max_length=6)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movies')),
            ],
            options={
                'verbose_name': 'Showtime',
                'verbose_name_plural': 'Showtimes',
            },
        ),
    ]
