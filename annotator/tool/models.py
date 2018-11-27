from django.db import models

class Annotation(models.Model):
    text = models.TextField('Document Text')
    file_name = models.CharField('File Name', blank=True)
    entities = models.ManytoManyField(Entity, )