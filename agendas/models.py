from django.db import models
from assisteds.models import AssistedsModel
from cooperators.models import CooperatorsModel


class AgendaModel(models.Model):

    id_assisted = models.ForeignKey(AssistedsModel, on_delete=models.PROTECT, blank=True, null=True)
    protocol = models.CharField(max_length=250, blank=True, null=True)
    date_at = models.DateField(blank=True, null=True)
    time_at= models.CharField(max_length=250, blank=True, null=True)
    status = models.CharField(max_length=1, default='0')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Atendimento com {self.id_assisted} no dia {self.date_at} às {self.time_at}"
