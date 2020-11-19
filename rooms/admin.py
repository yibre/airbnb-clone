from django.contrib import admin
from django.utils.html import mark_safe # 장고에게 사진을 믿을 수 있다는 확신을 주려고
from . import models

@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    list_display = (
        "name", "used_by"
    )

    def used_by(self, obj):
        return obj.rooms.count()


class PhotoInline(admin.StackedInline):
    model = models.Photo

@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    
    """Room Admin Definition"""

    inlines = (PhotoInline,)
    fieldsets = (
        (
            "Basic Info",
            {
                "fields": (
                    "name",
                    "description",
                    "country",
                    "city",
                    "address",
                    "price",
                    "room_type",
                )
            },
        ),
        ("Times", {"fields": ("check_in", "check_out", "instant_book")}),
        ("Spaces", {"fields": ("guests", "beds", "bedrooms", "baths")}),
        (
            "More About the Space",
            {"fields": ("amenities", "facilities", "house_rules")},
        ),
        ("Last Details", {"fields": ("host",)}),
    )

    list_display = (
        "name", "country", "city", "price", "guests", "beds", "bedrooms", "baths", "check_in", "check_out", 
        "instant_book", "count_amenities", "count_photos", "total_rating",
    )

    list_filter = ("instant_book", "host__superhost", "room_type", "amenities", "facilities", "house_rules", "city", "country",)
    
    raw_id_fields = ("host",)
    
    # seoul을 Seoul로 event intercept 하는 방법 seoul이라고 적어도 Seoul로 저장됨.
    # 아이템이 하나라고 해도 끝에 꼭 ,를 붙여줘야함. ("=city",) 이래야 형식이 유지됨.
    search_fields = ("=city", "^host__username")

    def count_amenities(self, obj):
        #self > roomadmin, obj > 현재 row
        # obj를 프린트하면 jousha tree house가 나옴
        # print(obj.amenities.all()) 하면 <QuerySet [<Amenity: Shower>]>가 나옴
        return obj.amenities.count()
    count_amenities.short_description = "hello sexy!"

    def count_photos(self, obj):
        return obj.photos.count()
        # rooms 안에 photos라는 related name이 있다는걸 앎

@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """ Photo Admin """
    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.file.url}" />')

    get_thumbnail.short_description = "Thumbnail"