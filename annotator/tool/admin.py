from django.contrib import admin
from .models import Annotation, Entity

class Entity_Admin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': (
                ('start', 'end'),
                ('phrase', 'entity_type')
            )}),
    )

    list_display = ('phrase', 'entity_type',)

class Annotation_Admin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': (
                ('file_name', 'entities'),
                'text',
                'file'
            )}),
    )

    list_display = ('file_name',)

# Register your models here.
admin.site.register(Annotation, Annotation_Admin)
admin.site.register(Entity, Entity_Admin)