# Generated by Django 4.1.5 on 2023-01-17 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QRcode',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=200)),
                ('link', models.TextField()),
            ],
        ),
    ]