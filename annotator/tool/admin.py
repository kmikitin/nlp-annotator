from django.contrib import admin
from .models import Annotation, Entity

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
admin.site.register(Entity)