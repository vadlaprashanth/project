# Generated by Django 4.1.5 on 2023-01-04 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiv1', '0003_remove_categories_departments_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='departments',
            name='categories',
            field=models.ManyToManyField(to='apiv1.categories'),
        ),
    ]