"""Movies app serializers"""

from django.utils import timezone

from rest_framework import serializers

from .models import Movie, Director


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate_birthday(self, birthday):
        if birthday > timezone.now().date():
            raise serializers.ValidationError(
                "El cumpleaños no puede estar en el futuro"
            )
        return birthday


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']


# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField()
#     director_id = serializers.IntegerField()
#     release_date = serializers.DateField()
#     stars = serializers.IntegerField()
#     sinopsis = serializers.CharField()
#     created_at = serializers.DateTimeField(read_only=True)
#     updated_at = serializers.DateTimeField(read_only=True)

#     def validate_stars(self, stars):
#         if stars > 5:
#             raise serializers.ValidationError(
#                 "No puede haber más de 5 estrellas"
#             )
#         return stars

#     def validate_director_id(self, director_id):
#         if not Director.objects.filter(id=director_id).exists():
#             raise serializers.ValidationError("El director no existe")
#         return director_id

#     def validate(self, validated_data):
#         title = validated_data.get("title")
#         director_id = validated_data.get("director_id")
#         movie_exists = Movie.objects.filter(
#             title=title, director_id=director_id
#         ).exists()
#         if movie_exists:
#             raise serializers.ValidationError("La película ya existe")
#         return validated_data

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)

#     def update(self, movie, validated_data):
#         movie.title = validated_data.get("title", movie.title)
#         movie.director_id = validated_data.get(
#             "director_id", movie.director_id
#         )
#         movie.release_date = validated_data.get(
#             "release_date", movie.release_date
#         )
#         movie.stars = validated_data.get("stars", movie.stars)
#         movie.sinopsis = validated_data.get("sinopsis", movie.sinopsis)
#         movie.save()
#         return movie
