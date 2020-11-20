"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings # 장고에서 setting을 import 하는 방법
from django.conf.urls.static import static # static 파일 제공을 도와주는 것들

urlpatterns = [
    path("", include("core.urls", namespace="core")),
    # view에 이름을 주려고 함. namespace가 의미하는 바는 다음에 설명해줄것.
    path("rooms/", include("rooms.urls", namespace="rooms")),
    path("admin/", admin.site.urls),
]

if settings.DEBUG: # 만약 DEBUG 모드가 true로 설정되어 있다면(즉 노란색 페이지가 뜬다면)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# media 폴더를 제공하고 싶다. 