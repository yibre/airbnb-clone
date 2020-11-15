from django.contrib import admin
from . import models

@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    """ Review Admin Definition """
    list_display = ("__str__", "rating_average")
    # 함수 호출 가능
    pass