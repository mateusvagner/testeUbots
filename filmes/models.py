from django.db import models

# Create your models here.
class Filme(models.Model):
    nome = models.CharField(max_length=100)
    avaliacao = models.DecimalField(max_digits=2, decimal_places=1)
    
    def __str__(self):
        return self.nome
    