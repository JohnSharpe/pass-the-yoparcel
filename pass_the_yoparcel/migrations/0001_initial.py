# Generated by Django 3.1.3 on 2020-11-06 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='MagicWord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField(unique=True)),
                ('word', models.CharField(max_length=200, unique=True)),
                ('message', models.CharField(max_length=200)),
                ('recipient', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='pass_the_yoparcel.person')),
            ],
        ),
    ]