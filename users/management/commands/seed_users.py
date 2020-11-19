from django.core.management.base import BaseCommand
from django_seed import Seed
from users.models import User


class Command(BaseCommand):

    help = "This command creates amenities"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="How many users you want to create"
        ) # default를 넣지 않으면 argument가 없을때 에러가 생김

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        seeder.add_entity(User, number, {"is_staff": False, "is_superuser": False}) # staff나 superuser를 만들지 않을 것
        # 이들이 admin 패널을 볼 수 있게 만들고 싶지 않음
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} users created!"))