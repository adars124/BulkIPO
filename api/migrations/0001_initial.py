# Generated by Django 4.2.4 on 2023-08-20 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clientId', models.PositiveIntegerField(default=0)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=100)),
                ('crn', models.CharField(max_length=50)),
                ('pin', models.CharField(max_length=50)),
            ],
        ),
    ]
