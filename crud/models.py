from django.db import models


class Marcas(models.Model):
    marca = models.CharField(max_length=500)
    sigla = models.CharField(max_length=100)

    def __str__(self):
        return self.marca


class Modelos(models.Model):
    modelo = models.CharField(max_length=500)
    sigla = models.CharField(max_length=100)
    marcas_id = models.ForeignKey(Marcas, on_delete=models.CASCADE)

    def __str__(self):
        return self.modelo


class Colores(models.Model):
    nombre = models.CharField(max_length=500)
    sigla = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Autos(models.Model):
    precio = models.IntegerField()
    descripcion = models.CharField(max_length=1024)
    modelo_id = models.ForeignKey(Modelos, on_delete=models.CASCADE)
    colores = models.ManyToManyField(Colores, related_name='AutosColores')

    def __str__(self):
        return self.descripcion
