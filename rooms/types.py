import graphene
from graphene_django import DjangoObjectType
from .models import Room


class RoomType(DjangoObjectType):

    user = graphene.Field("users.types.UserType")

    class Meta:
        model = Room


class RoomListResponse(graphene.ObjectType):
    room_list = graphene.List(RoomType)
    total = graphene.Int()