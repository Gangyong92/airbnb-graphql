import graphene
from .types import RoomType, RoomListResponse
from .queries import resolve_rooms, resolve_room


class Query(object):
    rooms = graphene.Field(
        RoomListResponse, page=graphene.Int(), resolver=resolve_rooms
    )
    room = graphene.Field(
        RoomType, id=graphene.Int(required=True), resolver=resolve_room
    )
