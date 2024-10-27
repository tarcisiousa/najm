from django.db import models


def documento_upload_to(instance, filename):
    # Monta o caminho com o PK do cliente
    return f'documents/assisteds{instance.id_assisted.pk}/{filename}'


class AssistedsModel(models.Model):
    choices_type_party = (
        ('Requerente', 'Requerente'),
    )
    choices_type_employee = (
        ('SIM', 'SIM'),
        ('NÃO', 'NÃO'),
    )
    choices_type_condition = (
        ('Capaz', 'Capaz'),
        ('Incapaz', 'Incapaz'),
    )
    choices_type_uf = (
        ('ACRE', 'AC'),
        ('ALAGOAS', 'AL'),
        ('AMAPÁ', 'AP'),
        ('AMAZONAS', 'AM'),
        ('BAHIA', 'BA'),
        ('CEARÁ', 'CE'),
        ('ESPÍRITO SANTO', 'ES'),
        ('GOIÁS', 'GO'),
        ('MARANHÃO', 'MA'),
        ('MATO GROSSO', 'MT'),
        ('MATO GROSSO DO SUL', 'MS'),
        ('MINAS GERAIS', 'MG'),
        ('PARÁ', 'PA'),
        ('PARAÍBA', 'PB'),
        ('PARANÁ', 'PR'),
        ('PERNAMBUCO', 'PE'),
        ('PIAUÍ', 'PI'),
        ('RIO DE JANEIRO', 'RJ'),
        ('RIO GRANDE DO NORTE', 'RN'),
        ('RIO GRANDE DO SUL', 'RS'),
        ('RONDÔNIA', 'RO'),
        ('RORAIMA', 'RR'),
        ('SANTA CATARINA', 'SC'),
        ('SÃO PAULO', 'SP'),
        ('SERGIPE', 'SE'),
        ('TOCANTINS', 'TO'),
    )
    choices_type_house = (
        ('Própria', 'Própria'),
        ('Cedida', 'Cedida'),
        ('Alugada', 'Alugada'),
    )
    party = models.CharField(max_length=100, choices=choices_type_party, default='Requerido')
    condition = models.CharField(max_length=100, choices=choices_type_condition, default='Capaz', blank=True)
    name = models.CharField(max_length=200)
    status_civil = models.CharField(max_length=200, blank=True)
    nis = models.CharField(max_length=200)
    rg = models.CharField(max_length=200, blank=True)
    organ = models.CharField(max_length=200, blank=True)
    date_birth = models.CharField(max_length=200, blank=True)
    date_expedition = models.CharField(max_length=200, blank=True)
    cpf = models.CharField(max_length=200, blank=True)
    email = models.CharField(max_length=200, blank=True)
    fone_1 = models.CharField(max_length=200, blank=True)
    fone_2 = models.CharField(max_length=200, blank=True)
    address = models.CharField(max_length=200, blank=True)
    district = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    uf = models.CharField(max_length=200, choices=choices_type_uf)
    dad = models.CharField(max_length=200, blank=True)
    mother = models.CharField(max_length=200, blank=True)
    employee = models.CharField(max_length=200, choices=choices_type_employee, blank=True)
    salary = models.CharField(max_length=200, blank=True)
    other_income = models.CharField(max_length=200, blank=True)
    dependents = models.CharField(max_length=200, blank=True)
    house = models.CharField(max_length=200, choices=choices_type_house, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name or "não tem nome"


class AssistedDocumentModel(models.Model):
    TYPE_DOCUMENT_CHOICES = [
        ('bens', 'Bens'),
        ('casamento', 'Casamento'),
        ('conta', 'Conta Bancária'),
        ('cpf', 'CPF'),
        ('dependentes', 'Dependentes'),
        ('filhos', 'Filhos'),
        ('nis', 'NIS'),
        ('obito', 'Óbito'),
        ('rendimentos', 'Rendimentos'),
        ('residencia', 'Comprovante de Residência'),
        ('reu', 'Réu'),
        ('rg', 'RG'),
        ('testemunhas', 'Testemunhas'),
        ('outro', 'Outros Documentos'),
    ]

    id_assisted = models.ForeignKey(AssistedsModel, related_name='documents_assisteds', on_delete=models.PROTECT)
    type_document = models.CharField(max_length=100, choices=TYPE_DOCUMENT_CHOICES, default='outro')
    name_customize = models.CharField(max_length=255, blank=True, null=True)  # Para novos tipos
    file = models.FileField(upload_to=documento_upload_to)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

