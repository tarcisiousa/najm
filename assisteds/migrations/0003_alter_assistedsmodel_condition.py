# Generated by Django 5.1.1 on 2024-10-27 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assisteds', '0002_alter_assistedsmodel_condition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assistedsmodel',
            name='condition',
            field=models.CharField(choices=[('Capaz', 'Capaz'), ('Incapaz', 'Incapaz')], default='Capaz', max_length=100),
        ),
    ]