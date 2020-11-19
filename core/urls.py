from django.urls import path
from rooms import views as room_views

app_name = "core" # 이것은 namespace를 위해 필요한 부분임

urlpatterns = [path("", room_views.all_rooms, name="home")]