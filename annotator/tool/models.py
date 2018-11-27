from django.db import models

class Entity(models.Model):

    class Meta:
        verbose_name = 'Entity'
        verbose_name_plural = 'Entities'

    start = models.IntegerField('Start Index')
    end = models.IntegerField('End Index')
    phrase = models.CharField('Word or Phrase', blank=True, max_length=250)
    entity_type = models.CharField('Entity Type', blank=True, max_length=50)

    def __str__(self):
        return '({}, {}, {})'.format(self.start, self.end, self.entity_type)


class Annotation(models.Model):
    text = models.TextField('Document Text', help_text='Should be one long string of parsed text')
    file_name = models.CharField('File Name', blank=True, null=True, max_length=500)
    file = models.FileField(upload_to='uploads/')
    entities = models.ManyToManyField(Entity, blank=True, verbose_name='Entities')