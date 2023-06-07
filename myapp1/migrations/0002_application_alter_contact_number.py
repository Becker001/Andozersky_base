# Generated by Django 4.2.1 on 2023-06-04 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('surname', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=100)),
                ('data', models.DateField()),
                ('data2', models.DateField()),
                ('place', models.IntegerField()),
                ('message', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='number',
            field=models.CharField(max_length=100),
        ),
    ]