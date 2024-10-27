from django.db import models


class SubModel(models.Model):
    protocol = models.CharField(max_length=250)
    processes_number = models.CharField(max_length=250)
    advocate_current = models.CharField(max_length=250)
    advocate_new = models.CharField(max_length=250)
    reason = models.TextField(max_length=250, help_text="Insira os motivos que justificaram a necessidade do substabelecimento.")
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.processes_number

