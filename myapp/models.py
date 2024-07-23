from django.db import models

class Autor(models.Model):
    Nombre = models.CharField('Nombre del autor', max_length = 30, null = False, blank = False)
    Apellido = models.CharField('Apellido del autor', max_length = 30, null = False, blank = False)
    Pintura = models.CharField('Estilo de pintura', max_length=50, null = False, blank = False)
    class Meta:
        db_table = "autores"
    def __str__(self):
        return self.Nombre + ' ' + self.Apellido

class Obra(models.Model):
    Titulo = models.CharField('Titulo de la Obra', max_length = 50, null = False, blank = False)
    Autor = models.ForeignKey(Autor, on_delete = models.DO_NOTHING)
    Fecha_Exposicion = models.DateField()

    class Meta:
        db_table = "obras"
    def __str__(self):
        return self.Titulo