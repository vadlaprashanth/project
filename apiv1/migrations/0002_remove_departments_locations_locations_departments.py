# Generated by Django 4.1.5 on 2023-01-04 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiv1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='departments',
            name='locations',
        ),
        migrations.AddField(
            model_name='locations',
            name='departments',
            field=models.ManyToManyField(to='apiv1.departments'),
        ),
    ]
