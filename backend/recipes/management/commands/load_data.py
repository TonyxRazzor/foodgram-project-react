import json
import logging
from django.core.management.base import BaseCommand

from recipes.models import Ingredient, Tag

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Загрузка данных в базу данных'

    def handle(self, *args, **options):
        try:
            with open('data/ingredients.json',
                      encoding='utf-8') as data_file_ingredients:
                ingredient_data = json.loads(data_file_ingredients.read())
                for ingredients in ingredient_data:
                    Ingredient.objects.get_or_create(**ingredients)

            with open('data/tags.json', encoding='utf-8') as data_file_tags:
                tags_data = json.loads(data_file_tags.read())
                for tags in tags_data:
                    Tag.objects.get_or_create(**tags)

            logger.success('Данные загружены')
        except Exception as e:
            logger.error(f'Ошибка при загрузке данных: {e}')

        self.stdout.write(self.style.SUCCESS('Данные успешно загружены'))
