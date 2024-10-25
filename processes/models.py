from django.db import models
from cooperators.models import CooperatorsModel
from responsibles.models import ResponsiblesModel
from assisteds.models import AssistedsModel
from requireds.models import RequiredsModel

def documento_upload_to(instance, filename):
    # Monta o caminho com o PK do cliente
    return f'documents/process{instance.id_process.pk}/{filename}'

class ProcessesModel(models.Model):
    choices_phase = (
        ('EM ANÁLISE', 'EM ANÁLISE'),
        ('PETIÇÃO', 'PETIÇÃO'),
        ('PROTOCOLADO', 'PROTOCOLADO'),
        ('FASE PROCESSUAL', 'FASE PROCESSUAL'),
        ('SENTENÇA', 'SENTENÇA'),
        ('ENCERRADO', 'ENCERRADO'),
    )
    choices_jurisdction = (
        ('SOBRADINHO', 'SOBRADINHO'),
    )

    protocol = models.CharField(max_length=200, default="0", blank=True, null=True)
    id_advocate = models.ForeignKey(CooperatorsModel, on_delete=models.PROTECT, blank=True, null=True)
    id_assisted = models.ForeignKey(AssistedsModel, on_delete=models.PROTECT, blank=True, null=True)
    id_responsible = models.ForeignKey(ResponsiblesModel, on_delete=models.PROTECT, blank=True, null=True)
    id_required = models.ForeignKey(RequiredsModel, on_delete=models.PROTECT, blank=True, null=True)
    facts = models.TextField(null=True, blank=True, help_text="Insira os fatos, narrativa ou detalhes relevantes...",
                             verbose_name="Fatos / Narrativa")
    number_process = models.CharField(max_length=200, blank=True, null=True)
    jurisdiction = models.CharField(max_length=200, blank=True, null=True, default='SOBRADINHO', choices=choices_jurisdction)
    processes_matter = models.CharField(max_length=200, blank=True, null=True)
    processes_classs = models.CharField(max_length=200, blank=True, null=True)
    processes_subject = models.CharField(max_length=200, blank=True, null=True)
    phase = models.CharField(max_length=200, choices=choices_phase, blank=True, null=True)
    date_at = models.DateField(blank=True, null=True)
    status_service = models.CharField(max_length=1, default='0', blank=True, null=True)
    notes = models.IntegerField(default=0, blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def get_subcategories(self):
        return self.action_subcategory_mapping.get(self.action, [])

    def __str__(self):
        return f'{self.protocol} - {self.date_at}' or 'Sem nome'

class ProcessDocumentModel(models.Model):
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
    id_process = models.ForeignKey(ProcessesModel, related_name='documents_processes', on_delete=models.PROTECT)
    type_document = models.CharField(max_length=100, choices=TYPE_DOCUMENT_CHOICES, default='outro')
    name_customize = models.CharField(max_length=255, blank=True, null=True)  # Para novos tipos
    file = models.FileField(upload_to=documento_upload_to)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)



class ProcessesNotesModel(models.Model):
    choices = (
        ('Baixa', 'Baixa'),
        ('Média', 'Média'),
        ('Alta', 'Alta'),
    )
    id_process = models.ForeignKey(ProcessesModel, related_name='note_process', on_delete=models.PROTECT)
    subject = models.CharField(max_length=200)
    note = models.TextField(max_length=500)
    user = models.CharField(max_length=250)
    priority = models.CharField(max_length=200, choices=choices)
    date_at = models.CharField(max_length=100)
    time_at = models.CharField(max_length=20)
    status = models.CharField(max_length=1, default=0, blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Assunto: {self.subject} - Usuário: {self.user}'