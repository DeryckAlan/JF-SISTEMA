from django.db import models

# Create your models here.
class Projeto(models.Model):
    cc = models.CharField(primary_key=True, max_length=255)
    projeto_name = models.CharField(max_length=200)
    
    def __str__(self):
        return f'{self.cc} - {self.projeto_name}'
    
class Painel(models.Model):
    painel_name = models.CharField(max_length=200)
    project_name = models.ForeignKey("Projeto", on_delete=models.PROTECT)
    
    def __str__(self):
        return self.painel_name