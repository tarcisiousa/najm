# Generated by Django 5.1.1 on 2024-10-24 12:32

import assisteds.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AssistedsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('party', models.CharField(choices=[('Requerente', 'Requerente')], default='Requerido', max_length=100)),
                ('condition', models.CharField(choices=[('Capaz', 'Capaz'), ('Incapaz', 'Incapaz')], default='Capaz', max_length=100)),
                ('name', models.CharField(max_length=200)),
                ('status_civil', models.CharField(blank=True, max_length=200)),
                ('nis', models.CharField(max_length=200)),
                ('rg', models.CharField(blank=True, max_length=200)),
                ('organ', models.CharField(blank=True, max_length=200)),
                ('date_birth', models.CharField(blank=True, max_length=200)),
                ('date_expedition', models.CharField(blank=True, max_length=200)),
                ('cpf', models.CharField(blank=True, max_length=200)),
                ('email', models.CharField(blank=True, max_length=200)),
                ('fone_1', models.CharField(blank=True, max_length=200)),
                ('fone_2', models.CharField(blank=True, max_length=200)),
                ('address', models.CharField(blank=True, max_length=200)),
                ('district', models.CharField(blank=True, max_length=200)),
                ('city', models.CharField(blank=True, max_length=200)),
                ('uf', models.CharField(choices=[('ACRE', 'AC'), ('ALAGOAS', 'AL'), ('AMAPÁ', 'AP'), ('AMAZONAS', 'AM'), ('BAHIA', 'BA'), ('CEARÁ', 'CE'), ('ESPÍRITO SANTO', 'ES'), ('GOIÁS', 'GO'), ('MARANHÃO', 'MA'), ('MATO GROSSO', 'MT'), ('MATO GROSSO DO SUL', 'MS'), ('MINAS GERAIS', 'MG'), ('PARÁ', 'PA'), ('PARAÍBA', 'PB'), ('PARANÁ', 'PR'), ('PERNAMBUCO', 'PE'), ('PIAUÍ', 'PI'), ('RIO DE JANEIRO', 'RJ'), ('RIO GRANDE DO NORTE', 'RN'), ('RIO GRANDE DO SUL', 'RS'), ('RONDÔNIA', 'RO'), ('RORAIMA', 'RR'), ('SANTA CATARINA', 'SC'), ('SÃO PAULO', 'SP'), ('SERGIPE', 'SE'), ('TOCANTINS', 'TO')], max_length=200)),
                ('dad', models.CharField(blank=True, max_length=200)),
                ('mother', models.CharField(blank=True, max_length=200)),
                ('employee', models.CharField(blank=True, choices=[('SIM', 'SIM'), ('NÃO', 'NÃO')], max_length=200)),
                ('salary', models.CharField(blank=True, max_length=200)),
                ('other_income', models.CharField(blank=True, max_length=200)),
                ('dependents', models.CharField(blank=True, max_length=200)),
                ('house', models.CharField(blank=True, choices=[('Própria', 'Própria'), ('Cedida', 'Cedida'), ('Alugada', 'Alugada')], max_length=200)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='AssistedDocumentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_document', models.CharField(choices=[('bens', 'Bens'), ('casamento', 'Casamento'), ('conta', 'Conta Bancária'), ('cpf', 'CPF'), ('dependentes', 'Dependentes'), ('filhos', 'Filhos'), ('nis', 'NIS'), ('obito', 'Óbito'), ('rendimentos', 'Rendimentos'), ('residencia', 'Comprovante de Residência'), ('reu', 'Réu'), ('rg', 'RG'), ('testemunhas', 'Testemunhas'), ('outro', 'Outros Documentos')], default='outro', max_length=100)),
                ('name_customize', models.CharField(blank=True, max_length=255, null=True)),
                ('file', models.FileField(upload_to=assisteds.models.documento_upload_to)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('id_assisted', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='documents_assisteds', to='assisteds.assistedsmodel')),
            ],
        ),
    ]
