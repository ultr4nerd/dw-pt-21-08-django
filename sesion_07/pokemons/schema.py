from asyncio.sslproto import _DO_HANDSHAKE
from dataclasses import asdict
from ssl import ALERT_DESCRIPTION_BAD_CERTIFICATE_HASH_VALUE
import graphene
from graphene_django import DjangoObjectType

from .models import Pokemon, Type


class TypeType(DjangoObjectType):
    class Meta:
        model = Type
        fields = '__all__'


class PokemonType(DjangoObjectType):
    class Meta:
        model = Pokemon
        fields = '__all__'


class CreateTypeMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)

    type = graphene.Field(TypeType)

    @classmethod
    def mutate(cls, root, info, name):
        types = Type.objects.filter(name=name)
        if types.exists():
            raise ValueError("El tipo ya existe")
        type = Type.objects.create(name=name)
        return CreateTypeMutation(type=type)


class CreatePokemonMutation(graphene.Mutation):
    pass


class Query:
    all_pokemons = graphene.List(PokemonType)
    all_types = graphene.List(TypeType)

    def resolve_all_pokemons(root, info):
        return Pokemon.objects.select_related("type").all()

    def resolve_all_types(root, info):
        return Type.objects.all()


class Mutation:
    create_type = CreateTypeMutation.Field()
