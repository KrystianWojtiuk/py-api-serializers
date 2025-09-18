from rest_framework.serializers import ModelSerializer

from cinema.models import CinemaHall, Genre, Actor, Movie, MovieSession


class CinemaHallSerializer(ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = '__all__'


class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class ActorSerializer(ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'


class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class MovieSessionSerializer(ModelSerializer):
    class Meta:
        model = MovieSession
        fields = '__all__'


