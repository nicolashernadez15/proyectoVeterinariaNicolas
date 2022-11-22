from django.db import models

# Create your models here.

class dueño(models.Model):

    dueño = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.CharField(max_length=50)
    sexo = models.CharField(max_length=50)

    class Meta:
        verbose_name = "dueño"
        verbose_name_plural = "dueños"

    def __str__(self):
        return self.dueño
    

class Mascota(models.Model):

    nombre = models.CharField(max_length=50)
    dueño = models.ForeignKey(dueño, on_delete=models.CASCADE)
    edad = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)

    class Meta:
        verbose_name = "mascota"
        verbose_name_plural = "mascotas"

    def __str__(self):
        return self.nombre
    
class ConsultaMedica(models.Model):
    nombre = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    fecha = models.CharField(max_length=100)
    motivo = models.CharField(max_length=100)
    diagnostico = models.CharField(max_length=100)
    tratamiento = models.CharField(max_length=100)
    observaciones = models.CharField(max_length=100)
    valor = models.IntegerField()

    class Meta:
        verbose_name = "ConsultasMedica"
        verbose_name_plural = "ConsultasMedicas"

    def __str__(self):
        return self.observaciones

class estetica(models.Model):
    nombre = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    fecha = models.CharField(max_length=100)
    motivo = models.CharField(max_length=100)
    diagnostico = models.CharField(max_length=100)
    tratamiento = models.CharField(max_length=100)
    observaciones = models.CharField(max_length=100)
    valor = models.IntegerField()

    class Meta:
        verbose_name = "estetica"
        verbose_name_plural = "esteticas"

    def __str__(self):
        return self.tratamiento


class vacuna(models.Model):
    nombre = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    fecha = models.CharField(max_length=100)
    motivo = models.CharField(max_length=100)
    diagnostico = models.CharField(max_length=100)
    tratamiento = models.CharField(max_length=100)
    observaciones = models.CharField(max_length=100)
    valor = models.IntegerField()

    class Meta:
        verbose_name = "vacuna"
        verbose_name_plural = "vacunas"

    def __str__(self):
        return self.motivo

class cirugia(models.Model):
    nombre = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    fecha = models.CharField(max_length=100)
    motivo = models.CharField(max_length=100)
    diagnostico = models.CharField(max_length=100)
    tratamiento = models.CharField(max_length=100)
    observaciones = models.CharField(max_length=100)
    valor = models.IntegerField()

    class Meta:
        verbose_name = "cirugia"
        verbose_name_plural = "cirugias"

    def __str__(self):
        return self.fecha
