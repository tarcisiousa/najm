# Generated by Django 5.1.1 on 2024-10-25 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='submodel',
            name='protocol',
            field=models.CharField(default=0, max_length=250),
            preserve_default=False,
        ),
    ]
