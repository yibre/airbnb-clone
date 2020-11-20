from django.utils import timezone
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.http import Http404
from . import models

# Create your views here.
class HomeView(ListView): # listview는 페이지를 찾음. 그리고 이들은 room_list라는 페이지를 찾고 있음

    """ HomeView Definition """

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "name" # ordering created 가 에러가 발생해서 이렇게 해둠
    page_kwarg = "potato"
    context_object_name = "rooms"

    def get_context_data(self, **kwargs):
    # 내가 사용하는 view가 하나의 기능만 사용할게 아니라서 씀
        context = super().get_context_data(**kwargs)
        now = timezone.now()
        context["now"] = now
        return context
"""
def room_detail(request, pk):
    try:
    # 만약 유저가 /rooms/125431654561 등의 번호를 적을 때를 대비하여
        room = models.Room.objects.get(pk=pk)
        return render(request, "rooms/detail.html", {"room":room})
    except models.Room.DoesNotExist:
        raise Http404()

"""
class RoomDetail(DetailView):
    """ Room Detail Definition """

    model = models.Room
    # Room을 받아서 lowercase로 바꾼 뒤 room을 템플릿 내의 room으로 넣음
    # Detail View는 raise 404 에러가 없어도 알아서 404페이지로 보내줌
