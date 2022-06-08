"""Movies app serializers"""

from rest_framework import serializers


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    director_id = serializers.IntegerField()
    release_date = serializers.DateField()
    stars = serializers.IntegerField()
    sinopsis = serializers.CharField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
