import graphene
from .models import Room
from .types import RoomType, RoomListResponse


class Query(object):
    rooms = graphene.Field(RoomListResponse, page=graphene.Int())
    room = graphene.Field(RoomType, id=graphene.Int(required=True))

    def resolve_rooms(self, info, page=1):
        if page < 1:
            page = 1
        page_size = 5
        skipping = page_size * (page - 1)
        taking = page_size * page
        rooms = Room.objects.all()[skipping:taking]
        total = Room.objects.count()
        return RoomListResponse(room_list=rooms, total=total)

    def resolve_room(self, info, id):
        return Room.objects.get(id=id)
