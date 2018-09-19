# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-08-16 19:24
from __future__ import unicode_literals

import json
import logging

from django.db import migrations
from osf.models import FileMetadataSchema

logger = logging.getLogger(__file__)


def add_datacite_schema(*args):
    with open('osf/metadata/schemas/datacite.json') as f:
        jsonschema = json.load(f)
    _, created = FileMetadataSchema.objects.get_or_create(
        _id='datacite',
        schema_version=1,
        defaults={
            'name': 'datacite',
            'schema': jsonschema
        }

    )
    if created:
        logger.info('Added datacite schema to the database')


def remove_datacite_schema(*args):
    FileMetadataSchema.objects.get(_id='datacite').delete()
    logger.info('Removed datacite schema from the database')


class Migration(migrations.Migration):

    dependencies = [
        ('osf', '0124_add_file_metadata_models'),
    ]

    operations = [
        migrations.RunPython(add_datacite_schema, remove_datacite_schema)
    ]
