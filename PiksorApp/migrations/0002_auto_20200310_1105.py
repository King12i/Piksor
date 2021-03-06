# Generated by Django 2.2 on 2020-03-10 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PiksorApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('series_name', models.CharField(max_length=45)),
                ('first_release_date', models.DateTimeField()),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='pixarcharacter',
            name='series',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='characters_in_series', to='PiksorApp.Series'),
            preserve_default=False,
        ),
    ]
