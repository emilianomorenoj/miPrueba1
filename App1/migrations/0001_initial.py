# Generated by Django 4.1.1 on 2022-09-14 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='familiares',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('número', models.IntegerField()),
                ('nombre', models.CharField(max_length=60)),
                ('fechanacimiento', models.DateField()),
            ],
        ),
    ]
