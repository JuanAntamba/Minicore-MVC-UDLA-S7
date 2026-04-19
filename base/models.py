from django.db import models

class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Nota(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=4, decimal_places=2)
    fecha = models.DateField()

    def __str__(self):
        return f"{self.alumno} - Nota: {self.valor} - Fecha: {self.fecha}" 