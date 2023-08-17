from django.db import models

# Create your models here.

class Plantas(models.Model):                  #hereda de moldels.model, en vez del SELF
    especie = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)     #elegis CharField o otro desde la lista que te recomienda models, maxLenght es una atributo
    precio = models.IntegerField()

    def __str__(self):
        return f"{self.especie}, {self.genero}, {self.precio}"
    
    class Meta:
        verbose_name = "Planta"
        verbose_name_plural = "Plantas"
        ordering = ['-genero']



class Macetas(models.Model):
    nombre= models.CharField(max_length=50)
    material= models.CharField(max_length=50)
    precio = models.IntegerField()
    
    def __str__(self):
        return f"{self.nombre}, {self.material}, {self.precio}"
    
    class Meta:
        verbose_name = "Maceta"
        verbose_name_plural = "Macetas"



class Jardineria(models.Model):
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    precio = models.IntegerField()

    def __str__(self):
        return f"{self.nombre}, {self.tipo}, {self.precio}"
    
    class Meta:
        verbose_name = "Jardineria"
        verbose_name_plural = "Jardineria"
        ordering = ['-tipo']

class Decoracion(models.Model):
    nombre= models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    precio = models.IntegerField()

    def __str__(self):
        return f"{self.nombre}, {self.tipo}, {self.precio}"
    
    class Meta:
        verbose_name = "Decoracion"
        verbose_name_plural = "Decoracion"
        ordering = ['-tipo']

class Usuarios(models.Model):
    nombre= models.CharField(max_length=50)
    nombre= models.CharField(max_length=50)
    email = models.EmailField()
    
    def __str__(self):
        return f"{self.nombre}, {self.email}"
    
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"




