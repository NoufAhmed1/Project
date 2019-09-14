# Generated by Django 2.2.3 on 2019-07-21 06:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typ', models.CharField(max_length=30)),
                ('phonenum', models.CharField(max_length=10)),
                ('price', models.CharField(max_length=7)),
                ('city', models.CharField(max_length=12)),
                ('start_on', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
