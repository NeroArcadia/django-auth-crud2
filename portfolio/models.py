from django.db import models

class project(models.Model):
    title = models.CharField(max_length= 100 , verbose_name='Titulo')
    description = models.TextField(verbose_name= 'Descripcion')
    image = models.ImageField(verbose_name='Imagen', upload_to= 'projects')
    created = models.DateTimeField(auto_now_add = True , verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now= True , verbose_name='Fecha de actualizacion')
    url = models.URLField(null= True , blank= True)
    
    def __str__(self):
        text = '{0}, {1}'
        return text.format(self.title, self.created)
    
class Meta:
    verbose_name = 'proyecto'
    verbose_name_plural = 'proyectos'
    ordering = ["-created"]