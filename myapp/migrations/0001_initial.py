# Generated by Django 4.1.7 on 2023-03-01 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('address', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.BigIntegerField()),
            ],
        ),
    ]
