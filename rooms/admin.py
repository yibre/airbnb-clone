from django.contrib import admin
from . import models

@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    
    """Room Admin Definition"""

    pass
# Register your models here.

@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """"""
    pass