from datetime import time

from django.core.management.base import BaseCommand
from shops.models import City, Street, Shop  # Убедитесь, что этот путь правильный


class Command(BaseCommand):
    help = 'Populate database with initial data'

    def handle(self, *args, **kwargs):
        cities = [
            {"name": "Москва"},
            {"name": "Санкт-Петербург"},
            {"name": "Новосибирск"}
        ]

        streets = [
            {"name": "Тверская", "city_name": "Москва"},
            {"name": "Невский проспект", "city_name": "Санкт-Петербург"},
            {"name": "Красный проспект", "city_name": "Новосибирск"}
        ]

        shops = [
            {"name": "Магазин 1", "city_name": "Москва", "street_name": "Тверская", "building": "1",
             "opening_time": time(9, 0), "closing_time": time(21, 0)},
            {"name": "Магазин 2", "city_name": "Санкт-Петербург", "street_name": "Невский проспект", "building": "2",
             "opening_time": time(10, 0), "closing_time": time(22, 0)},
            {"name": "Магазин 3", "city_name": "Новосибирск", "street_name": "Красный проспект", "building": "3",
             "opening_time": time(8, 0), "closing_time": time(20, 0)}
        ]

        for city_data in cities:
            city, created = City.objects.get_or_create(name=city_data["name"])
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created city: {city.name}'))

        for street_data in streets:
            city = City.objects.get(name=street_data["city_name"])
            street, created = Street.objects.get_or_create(name=street_data["name"], city=city)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created street: {street.name} in {city.name}'))

        for shop_data in shops:
            city = City.objects.get(name=shop_data["city_name"])
            street = Street.objects.get(name=shop_data["street_name"], city=city)
            shop, created = Shop.objects.get_or_create(
                name=shop_data["name"], city=city, street=street, building=shop_data["building"],
                opening_time=shop_data["opening_time"], closing_time=shop_data["closing_time"]
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created shop: {shop.name} in {street.name}, {city.name}'))
