from django.core.management.base import BaseCommand

from paczkomaty.models import Courier, Locker


class Command(BaseCommand):
    help = "Dodaje przykladowe paczkomaty i kurierow."

    def handle(self, *args, **options):
        lockers = [
            {"code": "WAW01", "city": "Warszawa", "address": "ul. Prosta 12", "capacity": 4},
            {"code": "KRA02", "city": "Krakow", "address": "ul. Dluga 8", "capacity": 3},
            {"code": "GDA03", "city": "Gdansk", "address": "ul. Morska 20", "capacity": 5},
        ]
        couriers = [
            {"full_name": "Anna Nowak", "phone": "500100200"},
            {"full_name": "Piotr Kowalski", "phone": "500300400"},
        ]

        for data in lockers:
            Locker.objects.get_or_create(code=data["code"], defaults=data)

        for data in couriers:
            Courier.objects.get_or_create(phone=data["phone"], defaults=data)

        self.stdout.write(self.style.SUCCESS("Dane startowe zostaly dodane."))
