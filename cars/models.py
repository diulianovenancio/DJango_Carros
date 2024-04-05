from django.db import models

class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200) #Tabela Modelo
    brand = models.CharField(max_length=200) #Tabela Marca
    factory_year = models.IntegerField(blank=True, null=True) #Tabela Ano de Fabricação
    model_year = models.IntegerField(blank=True, null=True) #Tabela Ano do Modelo
    value = models.FloatField(blank=True, null=True) #Tabela Valor

    def __str__(self) -> str:
        return self.model