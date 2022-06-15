"""Project schema"""
import graphene

from pokemons.schema import Query as PokemonsQuery, Mutation as PokemonsMutation


class Query(PokemonsQuery, graphene.ObjectType):
    ping = graphene.String()
    resta = graphene.Float(numa=graphene.Float(), numb=graphene.Float())

    def resolve_ping(root, info):
        return "Pong"

    def resolve_resta(root, info, numa, numb):
        return numa - numb


class Mutation(PokemonsMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
