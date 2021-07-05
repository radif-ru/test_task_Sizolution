import os
import json

from django.core.management.base import BaseCommand
from django.conf import settings


def load_from_json(file_name):
    with open(
            os.path.join(settings.JSON_PATH, f'{file_name}.json'),
            encoding='utf-8'
    ) as infile:
        return json.load(infile)


class Command(BaseCommand):
    help = 'Fill DB new data'

    # TODO: автоматизировать заполнение бд дефолтными данными
    def handle(self, *args, **options):
        pass
