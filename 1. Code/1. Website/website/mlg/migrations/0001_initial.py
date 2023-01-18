# Generated by Django 3.2.15 on 2023-01-18 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('repeat', models.IntegerField(default=1)),
                ('ignore', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('pseudo', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Parameters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=200)),
                ('value', models.CharField(max_length=200)),
                ('comment', models.CharField(max_length=1000)),
                ('action', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mlg.actions')),
            ],
        ),
        migrations.AddField(
            model_name='actions',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mlg.users'),
        ),
    ]