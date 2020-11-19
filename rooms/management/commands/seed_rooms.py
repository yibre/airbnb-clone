import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from django.contrib.admin.utils import flatten 
from rooms import models as room_models
from users import models as user_models


class Command(BaseCommand):

    help = "This command creates rooms"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="How many rooms you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder() 
        # 25명의 유저를 처음 가져오기
        all_users = user_models.User.objects.all() # 모든 유저를 database로부터 데려옴
        # 하지만 유저가 많으면 절대 all()해서 가져오면 안됨. 절대로.
        room_types = room_models.RoomType.objects.all() # roomtype이 null일수 없기때문에 전체 리스트를 가져옴
        seeder.add_entity(
            room_models.Room,
            number,
            {
                "name": lambda x: seeder.faker.address(), # faker db를 위해 엄청 많은 모듈을 가지고 있음
                "host": lambda x: random.choice(all_users), #랜덤한 host를 선택함
                "room_type": lambda x: random.choice(room_types), # 랜덤한 roomtype을 선택함
                "guests": lambda x: random.randint(1, 20),
                "price": lambda x: random.randint(1, 300),
                "beds": lambda x: random.randint(1, 5),
                "bedrooms": lambda x: random.randint(1, 5),
                "baths": lambda x: random.randint(1, 5),
            },
        )

        photo_list = [
            "https://a0.muscache.com/im/pictures/ce6814ba-ed53-4d6e-b8f8-c0bbcf821011.jpg?im_w=480",
            "https://a0.muscache.com/im/pictures/dd99d97f-adfb-455d-9518-594387707ac3.jpg?im_w=1200",
            "https://a0.muscache.com/im/pictures/968e83f7-3b11-44c5-a731-6fbf5677651a.jpg?im_w=1200",
            "https://a0.muscache.com/im/pictures/e131941c-d64b-4e30-8004-c19e0ea6903a.jpg?im_w=1200",
            "https://a0.muscache.com/im/pictures/51f4d564-3273-4f25-843d-54e17f6a8783.jpg?im_w=1200",
            "https://a0.muscache.com/im/pictures/89bfd8d4-b0e5-4110-b935-70c1e551991b.jpg?im_w=1440",
            "https://a0.muscache.com/im/pictures/4e2ef5f1-a6af-4525-87f5-c85bed4b7ebd.jpg?im_w=1200",
            "https://a0.muscache.com/im/pictures/7560313c-b286-4602-9e14-b0d190fde5f7.jpg?im_w=1440"
        ]

        created_photos = seeder.execute() # 리스트 안에 임의의 숫자를 생성함 [[14]]
        created_clean = flatten(list(created_photos.values())) # flatten 기능은 [[14]]를 [14]로 만들어줌
        amenities = room_models.Amenity.objects.all()
        facilities = room_models.Facility.objects.all()
        rules = room_models.HouseRule.objects.all()
            # Photo는 room을 가지고 있음. 이 둘을 연결할것임 room instance를 받아옴
        for pk in created_clean:
            room = room_models.Room.objects.get(pk=pk)
            for i in range(3, random.randint(4, 8)):
                room_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    room=room,
                    file=f"room_photos/{random.randint(1, 12)}.jpg",
                )
        for a in amenities:
            magic_number = random.randint(0, 15)
            if magic_number % 2 == 0:
                room.amenities.add(a) # 다대다 필드에서 무언가를 추가하는 방법
        for f in facilities:
            magic_number = random.randint(0, 15)
            if magic_number % 2 == 0:
                room.facilities.add(f)
        for r in rules:
            magic_number = random.randint(0, 15)
            if magic_number % 2 == 0:
                room.house_rules.add(r)
        self.stdout.write(self.style.SUCCESS(f"{number} rooms created!"))