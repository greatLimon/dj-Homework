import csv

from django.core.management.base import BaseCommand
from phones.models import Phone

from django.utils.text import slugify


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            # TODO: Добавьте сохранение модели
            Phone.objects.create(name = phone['name'], 
                                 image = phone['image'], 
                                 price = phone['price'], 
                                 release_data = phone['release_date'], 
                                 lte_exist = phone['lte_exists'],
                                 slug = slugify(phone['name'])
                                 )
