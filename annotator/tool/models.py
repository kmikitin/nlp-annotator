from django.db import models


class Label(models.Model):
    name = models.CharField('Label', max_length=30, help_text="the actual label whether from SpaCy or our own")
    description = models.TextField('Description', blank=True, help_text='Description of what the label should be used to tag, whether from SpaCy or our own.')

    def __str__(self):
        return '{}'.format(self.name)


class Entity(models.Model):

    class Meta:
        verbose_name = 'Entity'
        verbose_name_plural = 'Entities'

    start = models.IntegerField('Start Index')
    end = models.IntegerField('End Index')
    phrase = models.CharField('Word or Phrase', blank=True, max_length=250)
    entity_type = models.ForeignKey(Label, verbose_name='Label', on_delete=models.CASCADE)

    def __str__(self):
        return '({}, {}, {}, {})'.format(self.phrase, self.start, self.end, self.entity_type)


class Annotation(models.Model):
    text = models.TextField('Document Text', blank=True, editable=False, help_text='Should be one long string of parsed text')
    file_name = models.CharField('File Name', blank=True, null=True, max_length=500)
    file = models.FileField(upload_to='uploads/')
    entities = models.ManyToManyField(Entity, blank=True, verbose_name='Entities')

    def __str__(self):
        return '{}'.format(self.file_name)