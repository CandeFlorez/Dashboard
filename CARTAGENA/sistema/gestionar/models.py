from django.db import models


#Empleo
class fuerzaTrabajo(models.Model):
    meses = models.CharField(max_length=50)
    milesPersonas = models.FloatField()

    def __str__(self):
        return self.meses

class desempleo(models.Model):
    meses = models.CharField(max_length=50)
    porcentaje = models.FloatField()
    
    def __str__(self):
        return self.meses

#Pobreza
class pobrezaMonetaria(models.Model):
    año = models.IntegerField()
    porcentaje = models.FloatField()

    def __str__(self):
        return str(self.año)

class pobrezaExtrema(models.Model):
    año = models.IntegerField()
    porcentaje = models.FloatField()

    def __str__(self):
        return str(self.año)

#Educacion
class matriculaEscolar(models.Model):
    numeroMatriculas = models.IntegerField()
    año = models.IntegerField()

    def __str__(self):
        return str(self.año)

class matriculanivelEducatico(models.Model):
    nivel = models.CharField(max_length=50)
    porcentaje = models.FloatField()

    def __str__(self):
        return self.nivel

#Seguridad
class homicidios(models.Model):
    numeroMuertes = models.IntegerField()
    año = models.IntegerField()

    def __str__(self):
        return str(self.numeroMuertes)

class accidentes(models.Model):
    numeroAccidentes = models.IntegerField()
    año = models.IntegerField()
    
    def __str__(self):
        return str(self.numeroAccidentes)

class suicidios(models.Model):
    numeroSuicidios = models.IntegerField()
    año = models.IntegerField()

    def __str__(self):
        return str(self.numeroSuicidios)

#Movilidad
class atropellos(models.Model):
    numeroAtropellos = models.IntegerField()
    año = models.IntegerField()

    def __str__(self):
        return str(self.numeroAtropellos)


class comparendos(models.Model):
    año = models.IntegerField()
    motocicletas = models.IntegerField()
    automoviles = models.IntegerField()
    otros = models.IntegerField()

    def __str__(self):
        return str(self.año)



    









