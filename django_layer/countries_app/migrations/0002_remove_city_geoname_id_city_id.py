# Generated by Django 4.1.7 on 2023-03-14 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countries_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='geoname_id',
        ),
        migrations.AddField(
            model_name='city',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
