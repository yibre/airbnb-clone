from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
# User 모델을 inhereit 함
class User(AbstractUser): 
    """Custom User Model"""

    #constants
    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHERS = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHERS, "Other")
    )

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "kr"
    LANGUAGE_CHOICES = (
        #admin panel에서 보여질 일
        (LANGUAGE_ENGLISH, "English"),
        (LANGUAGE_KOREAN, "Korean")
    )

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"
    CURRENCY_CHOICES = ((CURRENCY_USD, "USD"), (CURRENCY_KRW, "KRW"))
    
    avatar = models.ImageField(blank=True)
    gender = models.CharField(choices = GENDER_CHOICES ,max_length = 10, blank=True)
    #gender filed는 비어있어도 괜찮다는 뜻.
    bio = models.TextField(blank=True)
    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length = 2, blank=True)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=3, blank=True)
    superhost = models.BooleanField(default=False)

    def __str__(self):
        return self.username