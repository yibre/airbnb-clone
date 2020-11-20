import os
from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models
from django.urls import reverse

class AbstractItem(core_models.TimeStampedModel):
    
    """ Absctract Item """
    name = models.CharField(max_length=80)

    class Meta:
        abstract=True

    def __str__(self):
        return self.name

class RoomType(AbstractItem):
    """ Room Type Object Definitions """
    # database에는 다른 필드가 들어가게 하기 위해서 이렇게 설정함.
    # users에서 했던 것처럼 우리가 직접 옵션을 설정할수도 있지만, 다른 언어로 옵션을 추가하고 싶다면, 즉 프로그래머 친화적인 방식이 아닌
    # 유저 친화적인 방식으로 하려면 이런 방법으로 해야함.
    class Meta:
        verbose_name = "Room Type"
        ordering = ["name"]

class Amenity(AbstractItem):
    """ Room Amenity """
    class Meta:
        verbose_name_plural = "Amenities"

class Facility(AbstractItem):
    """ Room Facility """
    class Meta:
        verbose_name_plural = "Facilities"

class HouseRule(AbstractItem):
    """ House Rule model definition """
    class Meta:
        verbose_name = "House Rule"


class Photo(core_models.TimeStampedModel):
    """ Photo Model Definition """
    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to="room_photos")
    room = models.ForeignKey("Room", related_name="photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption

class Room(models.Model):
    """Room Model Definition """
    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()# django Country package가 있음.
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    beds = models.IntegerField()
    baths = models.IntegerField()
    bedrooms = models.IntegerField()
    guests = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    #호스트는 users임. 모델을 다른 모델과 연결하는 방버이 있음.
    host = models.ForeignKey(
        "users.User", related_name="rooms", on_delete=models.CASCADE
    )
    room_type = models.ForeignKey(
        "RoomType", related_name="rooms", on_delete=models.SET_NULL, null=True
    ) # room type을 삭제한다고 room도 삭제되기를 원하진 않음
    amenities = models.ManyToManyField("Amenity", related_name="rooms", blank=True)
    facilities = models.ManyToManyField("Facility", related_name="rooms", blank=True)
    house_rules = models.ManyToManyField("HouseRule", related_name="rooms", blank=True)


    def save(self, *args, **kwargs):
        self.city = str.capitalize(self.city)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("rooms:detail", kwargs={"pk": self.pk})
    

    #모든 review의 average를 얻는 방법
    # review는 room을 가지고 있고 related name을 이용해 접근함
    def total_rating(self):
        all_reviews = self.reviews.all()
        all_ratings = 0
        if len(all_reviews) > 0: # room을 랜덤하게 생성하려고 할 때 review가 0이면 에러가 남
            for review in all_reviews:
                all_ratings += review.rating_average()
            return round(all_ratings / len(all_reviews), 2)
        return 0