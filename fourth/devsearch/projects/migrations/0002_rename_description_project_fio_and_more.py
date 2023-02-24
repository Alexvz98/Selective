# Generated by Django 4.1.7 on 2023-02-24 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='description',
            new_name='fio',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='featured_image',
            new_name='foto_image',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='demo_link',
            new_name='instagram_url',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='title',
            new_name='profession',
        ),
        migrations.RemoveField(
            model_name='project',
            name='source_link',
        ),
        migrations.RemoveField(
            model_name='project',
            name='vote_ratio',
        ),
        migrations.RemoveField(
            model_name='project',
            name='vote_total',
        ),
    ]