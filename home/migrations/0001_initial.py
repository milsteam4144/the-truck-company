# Generated by Django 2.2.4 on 2019-08-14 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Distributor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('address', models.TextField()),
                ('phone', models.CharField(max_length=20)),
                ('web_link', models.CharField(max_length=150)),
            ],
        ),
    ]
