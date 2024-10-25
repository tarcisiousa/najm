from django.db import models


class NotesModel(models.Model):
    choices = (
        ('Baixa', 'Baixa'),
        ('Média', 'Média'),
        ('Alta', 'Alta'),
    )
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
