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
    class Arguments:
        name = graphene.String(required=True)
        type = graphene.String(required=True)
        number = graphene.Int(required=True)

    pokemon = graphene.Field(PokemonType)

    @classmethod
    def mutate(cls, root, info, name, type, number):
        if Pokemon.objects.filter(number=number).exists():
            raise ValueError("No puede haber dos Pokémon con el mismo número")

        type_queryset = Type.objects.filter(name__iexact=type.strip())
        if type_queryset.exists():
            type_object = type_queryset.get()
        else:
            type_object = Type.objects.create(name=type.strip())

        pokemon = Pokemon.objects.create(
            name=name, type=type_object, number=number
        )
        return CreatePokemonMutation(pokemon=pokemon)


class Query:
    all_pokemons = graphene.List(PokemonType)
    all_types = graphene.List(TypeType)

    def resolve_all_pokemons(root, info):
        return Pokemon.objects.select_related("type").all()

    def resolve_all_types(root, info):
        return Type.objects.all()


class Mutation:
    create_type = CreateTypeMutation.Field()
    create_pokemon = CreatePokemonMutation.Field()
