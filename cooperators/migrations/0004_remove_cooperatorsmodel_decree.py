# Generated by Django 5.1.1 on 2024-10-24 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cooperators', '0003_alter_cooperatorsmodel_decree_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cooperatorsmodel',
            name='decree',
        ),
    ]
