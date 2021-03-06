# Generated by Django 2.2.10 on 2020-03-05 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0036_resourcebase_doi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curatedthumbnail',
            name='resource',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='base.ResourceBase'),
        ),
        migrations.AlterField(
            model_name='resourcebase',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='resourcebase',
            name='last_updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='resourcebase',
            name='regions',
            field=models.ManyToManyField(blank=True, help_text='keyword identifies a location', null=True, to='base.Region', verbose_name='keywords region'),
        ),
        migrations.AlterField(
            model_name='resourcebase',
            name='tkeywords',
            field=models.ManyToManyField(blank=True, help_text='formalised word(s) or phrase(s) from a fixed thesaurus used to describe the subject (space or comma-separated', null=True, to='base.ThesaurusKeyword', verbose_name='keywords'),
        ),
    ]
