from django.contrib import admin
from . import models

@admin.register(models.List)
class ListAdmin(admin.ModelAdmin):

    list_display = ("name", "user", "count_rooms")
    search_fields = ("name",) # search fields 에 ^name으로 시작하는걸 찾고 싶으면 이렇게 하면 됨
    filter_horizontal = ("rooms",)