from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


class ModelAudit(models.Model):
    isuso = models.BooleanField(default=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    estado = models.BooleanField(default=True)

    class Meta:
        abstract = True

# Create your models here.


class Encuesta(ModelAudit):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField()
    registro = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    num_pre_asig = models.PositiveIntegerField()
    isorden = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Likert(ModelAudit):
    denominacion = models.CharField(max_length=60)
    valor = models.PositiveIntegerField()
    encuesta = models.ForeignKey(Encuesta, on_delete=models.PROTECT)
    #para que aparezca el nombre, cuando se usa al admin de django
    def __str__(self):
        return self.denominacion


class Pregunta(ModelAudit):
  
    pregunta = models.CharField(max_length=100)
    registro = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    orden = models.PositiveIntegerField()
    tipo = models.PositiveIntegerField()
    encuesta = models.ForeignKey(Encuesta, on_delete=models.PROTECT)

    

    def __str__(self):
        return '{} -- {}- {}'.format(self.orden,self.encuesta.nombre, self.pregunta)


estados_civiles =(('S','SOLTERA'),
                  ('C','CONVIVIENTE')
                 
)

class Mujer(ModelAudit):
    ocupacion = models.CharField(max_length=40)
    estadocivil = models.CharField(max_length=1,choices=estados_civiles)
    nivel_educacion = models.CharField(max_length=60)
    hijos = models.PositiveIntegerField()
    edad = models.PositiveIntegerField()


class EncuestaMujer(ModelAudit):
    """
    for every question, the end time and num_pre_resuelta is updated
    """
    nombre = models.CharField(max_length=30)
    hora_inicio = models.TimeField(auto_now_add=True)
    hora_fin = models.TimeField(null=True)
    num_pre_asig = models.PositiveIntegerField()
    num_pre_resuelta = models.PositiveIntegerField()
    mujer = models.ForeignKey(Mujer, on_delete=models.PROTECT)
    encuesta = models.ForeignKey(Encuesta, on_delete=models.PROTECT)
    resultado = models.CharField(max_length=250,blank=True,null=True)
    def __str__(self):
        return self.nombre

    def decir_hola(self):
        return self.nombre + " " +" hola " 
    """
    make a function for asign a order
    1-- A
    2 --I
    3 -- D
    """
    def calcular(self):
        lista_preguntas=self.preguntaresultado_set.filter(estado=True)
        contadora=0
        contadori=0
        contadord=0
        
        for i in lista_preguntas:
            if i.pregunta.tipo == 1:
                contadora+=i.valor*(100/185)
            if i.pregunta.tipo == 2:
                contadori+=i.valor*(100/185)
            if i.pregunta.tipo == 3:
                contadord+=i.valor*(100/185)
                
        return [contadora,contadori,contadord,(contadori+contadord+contadora)]


"""
suma de algunas preguntas
"""
class Preguntaresultado(ModelAudit):
    pregunta_denom = models.CharField(max_length=100)
    valor = models.PositiveIntegerField()
    valor_denom = models.CharField(max_length=60)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.PROTECT)
    encuesta = models.ForeignKey(EncuestaMujer, on_delete=models.PROTECT)


