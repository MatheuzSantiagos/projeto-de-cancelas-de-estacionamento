from django.db import models

class Veiculo(models.Model):
    placa: str = models.CharField(max_length=10)
    modelo: str = models.CharField(max_length=100)
    cor: str = models.CharField(max_length=50)
    datahoraentrada: datetime = models.DatetimeField(auto_now_add=True)
    datahorasaida: datetime = models.DateTimeField(null=True, blank=True)
