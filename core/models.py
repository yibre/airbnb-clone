from django.db import models


class TimeStampedModel(models.Model):
    """ Time Stamped Model """
    created = models.DateTimeField(auto_now_add=True) # 모델을 생성하면 시간을 넘겨줌. 모델이 생성된 날짜.
    updated = models.DateTimeField(auto_now=True) # 저장할때마다 시간을 저장해줌. 새로운 날짜로 업데이트해줌.
    #이 모델이 database에 들어가기를 원하지 않음.

    class Meta:
        abstract = True
        # abstract model은 모델이지만 데이터베이스에서는 나타나지 않음.
        # user 에서 model을 보면 abstract user를 쓰는걸 알 수 있음.
# Create your models here.
