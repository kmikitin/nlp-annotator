# Generated by Django 2.1.3 on 2018-12-04 21:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Annotation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, help_text='Should be one long string of parsed text', verbose_name='Document Text')),
                ('file_name', models.CharField(blank=True, max_length=500, null=True, verbose_name='File Name')),
                ('file', models.FileField(upload_to='uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.IntegerField(verbose_name='Start Index')),
                ('end', models.IntegerField(verbose_name='End Index')),
                ('phrase', models.CharField(blank=True, max_length=250, verbose_name='Word or Phrase')),
            ],
            options={
                'verbose_name': 'Entity',
                'verbose_name_plural': 'Entities',
            },
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='the actual label whether from SpaCy or our own', max_length=30, verbose_name='Label')),
                ('description', models.TextField(blank=True, help_text='Description of what the label should be used to tag, whether from SpaCy or our own.', verbose_name='Description')),
            ],
        ),
        migrations.AddField(
            model_name='entity',
            name='entity_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tool.Label', verbose_name='Label'),
        ),
        migrations.AddField(
            model_name='annotation',
            name='entities',
            field=models.ManyToManyField(blank=True, to='tool.Entity', verbose_name='Entities'),
        ),
    ]
