# Generated by Django 5.1.1 on 2024-11-03 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cooperators', '0006_alter_cooperatorsmodel_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='cooperatorsmodel',
            name='status_civil',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
