# Generated by Django 3.0.3 on 2020-07-28 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0002_document_last_change_details'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='last_change_details',
        ),
    ]
