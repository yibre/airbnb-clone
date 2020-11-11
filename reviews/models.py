from django.db import models
from core import models as core_models
# Create your models here.

class Review(core_models.TimeStampedModel):
    
    """ Review Model Definition """
    
    review = models.TextField()
    accuracy = models.IntegerField()
    communication = models.IntegerField()
    cleanlines = models.IntegerField()
    location = models.IntegerField()
    check_in = models.IntegerField()
    value = models.IntegerField()
    user = models.ForeignKey("users.User", on_delete=models.CASCADE) # 유저가 삭제되면 리뷰도 삭제
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.review} - {self.room}"
        #return self.room.host.username # 3개의 레이어 안으로 들어감. room > host > user
        # return self.room.country 를 하면 KR이 뜸.