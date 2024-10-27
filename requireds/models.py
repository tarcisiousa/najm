from django.db import models
from assisteds.models import AssistedsModel

class RequiredsModel(models.Model):
    choices_type_kin = (
        ('Pai', 'Pai'),
        ('Mãe', 'Mãe'),
        ('Irmão(a)', 'Irmão(a)'),
        ('Tio(a)', 'Tio(a)'),
        ('Avô(a)', 'Avô(a)'),
        ('Outro', 'Outro'),

    )
    choices_type_employee = (
        ('SIM', 'SIM'),
        ('NÃO', 'NÃO'),
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
    id_assisted = models.ForeignKey(AssistedsModel, on_delete=models.PROTECT)
    kin = models.CharField(max_length=100, choices=choices_type_kin, default='Pai')
    name = models.CharField(max_length=200, blank=True, null=True)
    status_civil = models.CharField(max_length=200, blank=True, null=True)
    nit = models.CharField(max_length=200, blank=True, null=True)
    rg = models.CharField(max_length=200, blank=True, null=True)
    organ = models.CharField(max_length=200, blank=True, null=True)
    date_birth = models.CharField(max_length=200, blank=True, null=True)
    date_expedition = models.CharField(max_length=200, blank=True, null=True)
    cpf = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    fone_1 = models.CharField(max_length=200, blank=True, null=True)
    fone_2 = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    district = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    uf = models.CharField(max_length=200, choices=choices_type_uf, null=True)
    employee = models.CharField(max_length=200, choices=choices_type_employee, blank=True, null=True)
    salary = models.CharField(max_length=200, blank=True, null=True)
    other_income = models.CharField(max_length=200, blank=True, null=True)
    dependents = models.CharField(max_length=200, blank=True, null=True)
    house = models.CharField(max_length=200, choices=choices_type_house, blank=True, null=True)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name or "Responsável não definido"
