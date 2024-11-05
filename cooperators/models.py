from django.db import models

class CooperatorsModel(models.Model):
    choices_name = (
        ('Administrador(a)', 'Administrador(a)'),
        ('Advogado(a)', 'Advogado(a)'),
        ('Recepção', 'Recepção'),
        ('Procurador(a)', 'Procurador(a)'),
    )
    cargo_type_uf = (
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
    name = models.CharField(max_length=250)
    status_civil = models.CharField(max_length=200, blank=True)
    post = models.CharField(max_length=200, choices=choices_name)
    registration = models.CharField(max_length=250)
    cpf = models.CharField(max_length=250)
    number_order = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    fone_1 = models.CharField(max_length=200, default=0)
    fone_2 = models.CharField(max_length=200, default=0)
    address = models.CharField(max_length=200)
    district = models.CharField(max_length=200, default=0)
    city = models.CharField(max_length=200, default=0)
    uf = models.CharField(max_length=100, choices=cargo_type_uf)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name or 'Sem nome'
